"""Hybrid retrieval: reciprocal rank fusion of bm25 and dense, as rrf() in the 13 lab's pipeline.py.

Each document scores the sum of 1 / (k + rank) over the rankings it appears in, with k = 60.
It fuses full rankings, not top-10 lists, so a document 11th in both can still reach the fused top 10.
A score of 0 or less is not a match (bm25 pads with zero-score documents in docid order), so those
entries are left out of a ranking instead of adding a rank that only reflects the docid.

search_chunks does the same fusion over chunk rankings, so `p2 answer` can use hybrid.
p2.toml may name other systems or another k in a [hybrid] table: systems = ["bm25", "dense"], k = 60.
"""

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False


def rrf(rankings, k):
    fused: dict[str, float] = {}
    for ranking in rankings:
        for rank, (item, score) in enumerate((p for p in ranking if p[1] > 0), 1):
            fused[item] = fused.get(item, 0.0) + 1.0 / (k + rank)
    return order(fused.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        settings = cfg.table("hybrid")
        self.k = settings.get("k", 60)
        self.systems = [retrievers.build(name, corpus, cfg) for name in settings.get("systems", ["bm25", "dense"])]
        self.n_docs = len(corpus.docs)

    def search(self, text, k):
        return rrf([s.search(text, self.n_docs) for s in self.systems], self.k)[:k]

    def search_chunks(self, text, k):
        return rrf([s.search_chunks(text, len(s.chunks)) for s in self.systems], self.k)[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
