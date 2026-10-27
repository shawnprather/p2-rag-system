"""Pool judging candidates for the own gold set: every document in any system's top 10, plus exact
matches for code-like words in the query (snake_case, dotted names, @annotations, --flags, CamelCase).

    uv run python scripts/candidates.py QUERIES RUN [RUN ...] > pool.md

QUERIES is a queries file (qid, class, text, origin); each RUN is a run file of those queries.
It lists candidates only; whether one is relevant is decided by reading the document.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

DOCS = Path("corpora/own/docs")
CODE = re.compile(r"(?:--|@)?[A-Za-z_][\w.]*(?:_|\.|[a-z][A-Z])[\w.]*|--[\w-]+|@\w+")


def main(queries, *runs):
    titles = {p.stem: p.read_text(encoding="utf-8").split("\n", 1)[0][2:] for p in sorted(DOCS.glob("*.md"))}
    texts = {d: (DOCS / f"{d}.md").read_text(encoding="utf-8") for d in titles}
    ranks = defaultdict(lambda: defaultdict(dict))  # qid -> docid -> system -> rank
    for run in runs:
        for line in Path(run).read_text(encoding="utf-8").splitlines():
            qid, _, docid, rank, _, tag = line.split()
            ranks[qid][docid][tag] = int(rank)
    for line in Path(queries).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        qid, cls, text = line.split("\t")[:3]
        exact = {d for word in CODE.findall(text) for d, t in texts.items() if word in t}
        pool = set(ranks[qid]) | exact
        print(f"## {qid} ({cls}): {text}\n")
        for d in sorted(pool, key=lambda d: (min(ranks[qid][d].values(), default=99), d)):
            seen = ", ".join(f"{s} #{r}" for s, r in sorted(ranks[qid][d].items()))
            how = "; ".join(x for x in (seen, "exact match" if d in exact else "") if x)
            print(f"- `{d}` {titles[d]} ({how})")
        print()


if __name__ == "__main__":
    main(*sys.argv[1:])
