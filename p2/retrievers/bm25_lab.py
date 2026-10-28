"""Ablation of bm25: the same BM25 with the 12 lab's plain [a-z0-9]+ tokenizer instead of "codes".

Only the tokenizer changes; k1, b and the chunking stay as p2.toml sets them.
"codes" keeps a name such as physics_process whole and also indexes its parts, and "lab" keeps
only the parts, so the rare whole-name token is gone.
"""

from p2.retrievers import bm25

NEEDS_CLAUDE = False
BASE = "bm25"


def build(corpus, cfg):
    return bm25.BM25(corpus, cfg.replace(tokenizer="lab"))
