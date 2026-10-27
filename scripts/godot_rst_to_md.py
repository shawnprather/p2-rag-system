"""Convert the Godot 4.7 docs (reStructuredText) into Markdown files that `p2 ingest` reads.

    git clone --depth 1 --branch 4.7 https://github.com/godotengine/godot-docs.git ../p2-src/godot-docs
    uv run python scripts/godot_rst_to_md.py ../p2-src/godot-docs ../p2-raw/godot

Takes getting_started/ and tutorials/ (CC BY 3.0; classes/ is MIT and far too large, so it is left out).
Each page becomes <out>/<id>.md, "# <title>", a blank line and the body, where the id is the page's
path without "tutorials/" joined by "-" (tutorials/2d/2d_movement.rst -> 2d-2d_movement.md).
Pages of fewer than MIN_WORDS words (index pages that are only a table of contents) are skipped.
<out>-sources.tsv (beside <out>, so ingest never reads it) maps each id to its page on docs.godotengine.org, for the manifest's source column.
"""

import re
import sys
import textwrap
from pathlib import Path

SECTIONS = ("getting_started", "tutorials")
BASE_URL = "https://docs.godotengine.org/en/4.7/"
MIN_WORDS = 80

ADMONITIONS = {"note", "warning", "tip", "seealso", "important", "danger", "caution", "attention", "hint", "error"}
DROP = {"toctree", "image", "figure", "video", "raw", "include", "rst-class", "highlight", "only", "index", "meta", "contents"}
CODE = {"code-block", "code", "sourcecode", "code-tab", "literalinclude"}
UNDERLINE = re.compile(r"^([=\-~^*+#\"'`:.])\1{2,}\s*$")
DIRECTIVE = re.compile(r"^\.\.\s+([\w-]+)::\s*(.*)$")


def roles(text):
    """Roles and links, which may wrap across lines, so this also runs over a whole page."""
    text = re.sub(r":[\w:-]+:`([^`<]*?)\s*<[^`>]*>`", r"\1", text)  # :ref:`Node <class_Node>` -> Node
    text = re.sub(r":[\w:-]+:`~?([^`]*)`", lambda m: m.group(1).split(".")[-1] if m.group(1).startswith("class_") else m.group(1), text)
    text = re.sub(r"(?<!`)`([^`<]+?)\s*<[^`>]+>`__?", r"\1", text)  # `text <url>`_ -> text
    return re.sub(r"(?<!`)`([^`]+)`__", r"\1", text)


def inline(text):
    text = roles(text)
    text = re.sub(r"(?<!`)`([^`]+)`_", r"\1", text)
    text = re.sub(r"``([^`]+)``", r"`\1`", text)
    text = re.sub(r"\|[\w -]+\|", "", text)  # substitutions such as |image0|
    return text


def block(lines, start, indent):
    """The indented body that follows lines[start - 1], and the index after it."""
    end = start
    while end < len(lines) and (not lines[end].strip() or len(lines[end]) - len(lines[end].lstrip()) > indent):
        end += 1
    body = textwrap.dedent("\n".join(lines[start:end])).split("\n")
    while body and body[0].lstrip().startswith(":") and not body[0].lstrip().startswith("::"):
        body.pop(0)  # directive options such as :alt: or :linenos:
    return body, end


def convert(lines):
    out, i, heading = [], 0, 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())
        if stripped.startswith(".. _") and stripped.endswith(":"):  # a link target
            i += 1
            continue
        m = DIRECTIVE.match(stripped)
        if m:
            name, arg = m.group(1).lower(), m.group(2).strip()
            body, i = block(lines, i + 1, indent)
            if name in DROP:
                continue
            if name in CODE:
                label = (arg.split(None, 1)[-1] if arg else "") if name == "code-tab" else ""
                if label:
                    out.append(f"{label}:")
                out += ["```", *body, "```"] if name != "literalinclude" else []
            elif name in ADMONITIONS:
                out += [f"{name.capitalize()}: " + " ".join(inline(b) for b in convert(body) if b.strip())]
            else:  # tabs, tab, table, list-table, container and the like keep their content
                if arg and name not in {"tabs", "container"}:
                    out.append(inline(arg))
                out += convert(body)
            continue
        if stripped.startswith(".."):  # a comment, and its indented continuation
            _, i = block(lines, i + 1, indent)
            continue
        if UNDERLINE.match(stripped) and i + 1 < len(lines) and lines[i + 1].strip() and i + 2 < len(lines) and UNDERLINE.match(lines[i + 2].strip()):
            i += 1  # an overline: the heading comes next
            continue
        if stripped and i + 1 < len(lines) and UNDERLINE.match(lines[i + 1].strip()) and len(lines[i + 1].strip()) >= len(stripped) - 1:
            heading += 1
            out.append(("# " if heading == 1 else "## ") + inline(stripped))
            out.append("")
            i += 2
            continue
        if stripped.endswith("::") and not stripped.startswith(".."):  # a paragraph that ends in a literal block
            text = stripped[:-2].rstrip()
            if text:
                out.append(inline(line[:indent] + text + ":"))
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and len(lines[j]) - len(lines[j].lstrip()) > indent:
                body, i = block(lines, j, indent)
                out += ["```", *body, "```"]
            else:
                i += 1
            continue
        out.append(inline(line))
        i += 1
    return out


def page(path):
    md = convert(path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(l.rstrip() for l in md)).strip() + "\n"
    if not text.startswith("# "):
        return None
    title, _, body = roles(text).partition("\n")
    return f"{title}\n\n{body.strip()}\n"


def main(src, out):
    src, out = Path(src), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    sources, kept, skipped = [], 0, 0
    for section in SECTIONS:
        for path in sorted((src / section).rglob("*.rst")):
            rel = path.relative_to(src).with_suffix("")
            parts = rel.parts[1:] if rel.parts[0] == "tutorials" else rel.parts
            docid = "-".join(parts).lower()
            text = page(path)
            if text is None or len(text.split()) < MIN_WORDS:
                skipped += 1
                continue
            (out / f"{docid}.md").write_text(text, encoding="utf-8", newline="\n")
            sources.append(f"{docid}\t{BASE_URL}{rel.as_posix()}.html")
            kept += 1
    (out.parent / f"{out.name}-sources.tsv").write_text("\n".join(sources) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {kept} pages to {out}, skipped {skipped} under {MIN_WORDS} words or with no title")


if __name__ == "__main__":
    main(*sys.argv[1:3])
