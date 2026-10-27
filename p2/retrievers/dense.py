"""Dense retrieval: embed every chunk once, embed the query, and rank chunks by cosine similarity.

It is the embedding arm of the 12 lab's retrieve.py (dense_rankings) over chunks instead of whole
articles: p2/embed.py loads the model and caches the chunk vectors in .cache/vectors/, and since
every vector has length 1, one matrix product gives the cosine similarity of the query to every chunk.

The model is bge-small-en-v1.5 unless p2.toml has a [dense] table with model = "...".
"""

import numpy as np

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.model = cfg.table("dense").get("model", embed.BGE)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> np.ndarray:
        if not len(self.chunks):
            return np.zeros(0, dtype=np.float32)
        query = self.embedder.encode([text])[0]
        return self.vectors @ query


def build(corpus, cfg):
    return Dense(corpus, cfg)
