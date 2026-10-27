"""Listwise reranking: Claude reorders hybrid's top 20, as rerank_one() in the 13 lab's pipeline.py.

The 20 candidates go to Claude as numbered passages, and RERANK_SCHEMA forces the reply into
{"order": [20 numbers]}, each between 1 and 20. A reply that is not each number once (or no reply)
keeps the first-stage order, and the candidates below the top 20 keep their order underneath.

A document is shown through its best chunk in hybrid's fused chunk ranking, not its first words,
so a long section shows the part that matched. search_chunks reranks hybrid's top 20 chunks the same
way, which is what `p2 answer --system rerank` uses.
"""

from p2 import claude, retrievers
from p2.corpus import docid_of

NEEDS_CLAUDE = True
CANDIDATES = 20

PROMPT = """Rank these passages by how well they answer the search query.
A passage that states what the query asks about ranks above one that only mentions it or refers to another section.

Query: {query}

{passages}

Reply with the numbers of all {n} passages, each once, most relevant first."""


def schema(n):
    return {
        "type": "object",
        "properties": {
            "order": {"type": "array", "items": {"type": "integer", "minimum": 1, "maximum": n}, "minItems": n, "maxItems": n}
        },
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg, first_stage="hybrid", candidates=CANDIDATES):
        self.cfg = cfg
        self.model = cfg.model
        self.candidates = candidates
        self.first = retrievers.build(first_stage, corpus, cfg)
        self.chunks = corpus.chunks(cfg.chunk_words, cfg.chunk_overlap)
        self.chunk_text = {c.id: c.text for c in self.chunks}
        self.first_chunk = {}
        for c in self.chunks:
            self.first_chunk.setdefault(c.docid, c.id)

    def rerank(self, query, ranking, texts):
        """ranking: the first stage's (id, score) list; texts: the passage for each id in its top candidates."""
        top, rest = ranking[: self.candidates], ranking[self.candidates :]
        n = len(top)
        if n < 2:
            return ranking
        passages = "\n\n".join(f"[{i}] {texts[item]}" for i, (item, _) in enumerate(top, 1))
        reply = claude.call(
            PROMPT.format(query=query, passages=passages, n=n), schema(n),
            model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg),
        )  # fmt: skip
        order = (reply.output or {}).get("order")
        if not isinstance(order, list) or sorted(order) != list(range(1, n + 1)):
            order = list(range(1, n + 1))  # a malformed reply keeps the first-stage order
        reranked = [top[i - 1][0] for i in order] + [item for item, _ in rest]
        return [(item, 1.0 / rank) for rank, item in enumerate(reranked, 1)]

    def search(self, text, k):
        ranking = self.first.search(text, max(k, self.candidates))
        best = {}
        for chunk_id, _ in self.first.search_chunks(text, len(self.chunks)):
            best.setdefault(docid_of(chunk_id), chunk_id)
        texts = {d: self.chunk_text[best.get(d, self.first_chunk[d])] for d, _ in ranking[: self.candidates]}
        return self.rerank(text, ranking, texts)[:k]

    def search_chunks(self, text, k):
        ranking = self.first.search_chunks(text, max(k, self.candidates))
        return self.rerank(text, ranking, self.chunk_text)[:k]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
