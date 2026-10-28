# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

Dense is bge-small-en-v1.5 which was done in 300 word chunks with 50 words of overlap. It was with cosine similarity where a page scores with its highest chunk. bge was tested and was better than potion.

Hybrid uses reciprocal rank fusion with a k of 60 for bm25 and then dense over their rankings.

Lastly Rerank is just hybrid but the claude sonnet reorders the top 20 results. Each page shows its best chunk. If the claude response errors it just revets to the original.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.617 | 0.471 | 0.456 |
| rerank | 0.725 | 0.750 | 0.727 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.571 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.435 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.500 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.571 | 1.000 |
| rerank | nDCG@10 | 0.703 | 0.516 | 1.000 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.008 | [-0.225, +0.208] | 0.317 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.062 | [-0.218, +0.082] | 0.218 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.058 | [-0.117, +0.242] | 0.261 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.023 | [-0.193, +0.137] | 0.240 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.100 | [-0.125, +0.325] | 0.331 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.243 | [+0.010, +0.476] | 0.339 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.208 | [-0.012, +0.423] | 0.317 | not distinguishable |
| rerank minus dense | Recall@10 | +0.167 | [-0.025, +0.350] | 0.271 | not distinguishable |
| rerank minus dense | MRR@10 | +0.188 | [-0.017, +0.392] | 0.294 | not distinguishable |
| rerank minus dense | nDCG@10 | +0.247 | [+0.062, +0.423] | 0.264 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.108 | [+0.025, +0.209] | 0.141 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | 0.230 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.270 | [+0.156, +0.392] | 0.171 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?

The two distinguishable pairs are rerank-hybrid and rerank-bm25. The rest are not distinguishable to differing amounts.

What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?

So 0.19 which is hybrid-bm25 up to 0.41 which is dense-bm25. So any gap smaller than 0.2-0.4 we can't make results from. So with just 20 queries we basiclly just can't tell.

Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

One of the main claims that lecture 12 that was supported was that of the fact that no retriever wins everywhere. Both bm25 and dense are good at different things bm25 for identifier and dense for paraphrase. Then for lecture 13 the main thing that was supported was just that rerankers are very good at improving results. I couldn't tell if hybrid fusion.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 9 of 9 |
<!-- p2:end answers -->

Which system answered, and why that one?

Rerank did because it had the best practice MRR of 0.75 and it beat hybrid so it is the best to provide the best chunks to claude.

What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Nothing since the results were verified and declined as they should have been. So nothing moved.

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

a02: supports, it gave a good qoute back which was acurate but missed out on supplying evidence for the fact about methane.

a05: supports, it gives a qoute that is the direct original of what it was saying.

a08: doesn't support, the claim was talking about breathable air not about food and water although they are related so it is close ish but not supported by the qoute.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

It is from the Godot Engine 4.7 docs which is a game making engine. It came from the documentation repo. It is 353 documents, 508k words, 3.5 MB. Its License is CC BY 3.0 to Juan Linietsky, Ariel Manzur and the Godot community. The documents I was least sure about was the actual classes folder which was under a different license being MIT and is 1.58M words so too much to cover.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

34 queries, 10 handwritten, 24 claude written. Classes are identifier, paraphrase, and mixed. This was to keep similarity with the shared set. Most of them were paraphrase since that was the main thing I wanted to target. 

Relevance rule is that a page that is explaining how to do something is most relavant and if 2D is mentioned then the results should be 2D and vise virsa if 3D no overlap if possible.

Candidates were found from the4 top 10 of all four systems bm25, dense, hybrid, rerank, and an exact match search which snippets shown for the judging of each. 

Yes, I did read every document before labeling it and then I also had Claude check over my work to make sure I didn't miss anything that was hard to confirm (Since godot is kinda complex especially with shader and physics stuff).

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.713 | 0.574 | 0.572 |
| dense | 0.760 | 0.712 | 0.659 |
| hybrid | 0.833 | 0.671 | 0.683 |
| rerank | 0.902 | 0.941 | 0.879 |
| ablation/bm25_lab | 0.706 | 0.561 | 0.555 |

34 judged queries; nDCG uses binary labels; a random ranking of the 353 documents would get recall@10 near 0.028.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=8) | paraphrase (n=16) | mixed (n=10) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.406 | 0.975 |
| bm25 | MRR@10 | 1.000 | 0.237 | 0.773 |
| bm25 | nDCG@10 | 0.980 | 0.239 | 0.778 |
| dense | Recall@10 | 0.875 | 0.693 | 0.775 |
| dense | MRR@10 | 0.938 | 0.481 | 0.900 |
| dense | nDCG@10 | 0.846 | 0.492 | 0.777 |
| hybrid | Recall@10 | 1.000 | 0.646 | 1.000 |
| hybrid | MRR@10 | 1.000 | 0.382 | 0.870 |
| hybrid | nDCG@10 | 0.950 | 0.436 | 0.865 |
| rerank | Recall@10 | 1.000 | 0.792 | 1.000 |
| rerank | MRR@10 | 1.000 | 0.875 | 1.000 |
| rerank | nDCG@10 | 0.985 | 0.769 | 0.972 |
| ablation/bm25_lab | Recall@10 | 1.000 | 0.406 | 0.950 |
| ablation/bm25_lab | MRR@10 | 0.938 | 0.236 | 0.778 |
| ablation/bm25_lab | nDCG@10 | 0.928 | 0.240 | 0.760 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=24) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.650 | 0.740 | -0.090 | [-0.365, +0.183] | not distinguishable |
| bm25 | MRR@10 | 0.456 | 0.624 | -0.168 | [-0.452, +0.130] | not distinguishable |
| bm25 | nDCG@10 | 0.427 | 0.632 | -0.205 | [-0.435, +0.025] | not distinguishable |
| dense | Recall@10 | 0.817 | 0.736 | +0.081 | [-0.174, +0.310] | not distinguishable |
| dense | MRR@10 | 0.703 | 0.715 | -0.012 | [-0.303, +0.269] | not distinguishable |
| dense | nDCG@10 | 0.647 | 0.664 | -0.017 | [-0.240, +0.195] | not distinguishable |
| hybrid | Recall@10 | 0.892 | 0.809 | +0.083 | [-0.095, +0.269] | not distinguishable |
| hybrid | MRR@10 | 0.570 | 0.713 | -0.143 | [-0.390, +0.113] | not distinguishable |
| hybrid | nDCG@10 | 0.652 | 0.696 | -0.045 | [-0.257, +0.170] | not distinguishable |
| rerank | Recall@10 | 0.942 | 0.885 | +0.056 | [-0.065, +0.189] | not distinguishable |
| rerank | MRR@10 | 0.950 | 0.938 | +0.013 | [-0.108, +0.146] | not distinguishable |
| rerank | nDCG@10 | 0.896 | 0.873 | +0.023 | [-0.101, +0.154] | not distinguishable |
| ablation/bm25_lab | Recall@10 | 0.625 | 0.740 | -0.115 | [-0.390, +0.167] | not distinguishable |
| ablation/bm25_lab | MRR@10 | 0.453 | 0.606 | -0.153 | [-0.441, +0.143] | not distinguishable |
| ablation/bm25_lab | nDCG@10 | 0.405 | 0.617 | -0.213 | [-0.430, +0.005] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.003 | -0.167 | +0.170 | [-0.197, +0.502] | not distinguishable |
| MRR@10 | -0.092 | -0.247 | +0.156 | [-0.144, +0.466] | not distinguishable |
| nDCG@10 | -0.032 | -0.220 | +0.189 | [-0.051, +0.428] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.67 (10 queries), claude 0.83 (24 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 24 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | +0.047 | [-0.108, +0.206] | 0.224 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.137 | [+0.021, +0.264] | 0.174 | dense higher |
| dense minus bm25 | nDCG@10 | +0.087 | [-0.016, +0.193] | 0.151 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.120 | [+0.044, +0.218] | 0.126 | hybrid higher |
| hybrid minus bm25 | MRR@10 | +0.097 | [+0.022, +0.175] | 0.110 | hybrid higher |
| hybrid minus bm25 | nDCG@10 | +0.111 | [+0.056, +0.170] | 0.083 | hybrid higher |
| hybrid minus dense | Recall@10 | +0.074 | [-0.074, +0.221] | 0.212 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.041 | [-0.151, +0.067] | 0.159 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.024 | [-0.065, +0.109] | 0.125 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.189 | [+0.083, +0.309] | 0.164 | rerank higher |
| rerank minus bm25 | MRR@10 | +0.367 | [+0.226, +0.509] | 0.207 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.308 | [+0.196, +0.423] | 0.166 | rerank higher |
| rerank minus dense | Recall@10 | +0.142 | [+0.010, +0.279] | 0.196 | rerank higher |
| rerank minus dense | MRR@10 | +0.229 | [+0.093, +0.373] | 0.205 | rerank higher |
| rerank minus dense | nDCG@10 | +0.220 | [+0.104, +0.344] | 0.174 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.069 | [+0.000, +0.152] | 0.108 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.270 | [+0.141, +0.407] | 0.195 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.196 | [+0.095, +0.304] | 0.154 | rerank higher |
| ablation/bm25_lab minus bm25 | Recall@10 | -0.007 | [-0.022, +0.000] | 0.021 | not distinguishable |
| ablation/bm25_lab minus bm25 | MRR@10 | -0.014 | [-0.045, +0.004] | 0.042 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | -0.017 | [-0.040, +0.002] | 0.031 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | -0.054 | [-0.211, +0.100] | 0.224 | not distinguishable |
| ablation/bm25_lab minus dense | MRR@10 | -0.151 | [-0.276, -0.032] | 0.175 | dense higher |
| ablation/bm25_lab minus dense | nDCG@10 | -0.104 | [-0.208, -0.003] | 0.148 | dense higher |
| ablation/bm25_lab minus hybrid | Recall@10 | -0.127 | [-0.225, -0.049] | 0.129 | hybrid higher |
| ablation/bm25_lab minus hybrid | MRR@10 | -0.110 | [-0.191, -0.033] | 0.115 | hybrid higher |
| ablation/bm25_lab minus hybrid | nDCG@10 | -0.128 | [-0.187, -0.072] | 0.084 | hybrid higher |
| ablation/bm25_lab minus rerank | Recall@10 | -0.196 | [-0.314, -0.088] | 0.165 | rerank higher |
| ablation/bm25_lab minus rerank | MRR@10 | -0.380 | [-0.519, -0.242] | 0.205 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.325 | [-0.437, -0.215] | 0.162 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?

The differences that are distinguishable are rerank-hybrid, rerank-dense, rerank-bm25, and hybrid-bm25. The ones that aren't dense-bm25, and hybrid-dense.

Do the `hand` queries and the `claude` queries tell the same story?

mostly, rerank is the best for both. bm25 does significantly worse for the handwritten ones because there isn't as many direct word hits as there is in the claude wrote ones. Also most of mine are paraphrase so it skews that direction.

Did your prediction in `DECISIONS.md` prompt 1 hold?

Yes my predictions held very well. I think the learning from lesson 12, 13 and learning about the different types of systems helped a lot in perdicting it I mean also in general bm25 is kinda bad and rerank is pretty good unsuprisingly.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

I expect switching from codes to the lab tokenizer on bm25 to lower nDCG@10 because the score for hits on rare words won't effect the score returned unlike codes meaning that in theory like physics_process will return a bunch more stuff about physics and process and won't filter stuff about physics_process as much.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/bm25_lab minus bm25 | Recall@10 | -0.007 | [-0.022, +0.000] | 0.021 | not distinguishable |
| ablation/bm25_lab minus bm25 | MRR@10 | -0.014 | [-0.045, +0.004] | 0.042 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | -0.017 | [-0.040, +0.002] | 0.031 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | -0.054 | [-0.211, +0.100] | 0.224 | not distinguishable |
| ablation/bm25_lab minus dense | MRR@10 | -0.151 | [-0.276, -0.032] | 0.175 | dense higher |
| ablation/bm25_lab minus dense | nDCG@10 | -0.104 | [-0.208, -0.003] | 0.148 | dense higher |
| ablation/bm25_lab minus hybrid | Recall@10 | -0.127 | [-0.225, -0.049] | 0.129 | hybrid higher |
| ablation/bm25_lab minus hybrid | MRR@10 | -0.110 | [-0.191, -0.033] | 0.115 | hybrid higher |
| ablation/bm25_lab minus hybrid | nDCG@10 | -0.128 | [-0.187, -0.072] | 0.084 | hybrid higher |
| ablation/bm25_lab minus rerank | Recall@10 | -0.196 | [-0.314, -0.088] | 0.165 | rerank higher |
| ablation/bm25_lab minus rerank | MRR@10 | -0.380 | [-0.519, -0.242] | 0.205 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.325 | [-0.437, -0.215] | 0.162 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/bm25_lab against bm25 (BASE = "bm25" in p2/retrievers/bm25_lab.py): it helped 3 queries, hurt 2 and left 29 unchanged.

| Query | Class | Origin | bm25 RR | ablation/bm25_lab RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| c24 | mixed | claude | 0.200 | 0.250 | +0.050 | helped |
| c15 | paraphrase | claude | 0.100 | 0.125 | +0.025 | helped |
| h01 | paraphrase | hand | 0.111 | 0.125 | +0.014 | helped |
| c08 | identifier | claude | 1.000 | 0.500 | -0.500 | hurt |
| h05 | paraphrase | hand | 0.250 | 0.200 | -0.050 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

TODO: write the ablation: the one change, the hypothesis, the result and the claim.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|

TODO: add one row for each failure you analyzed, and write two or three sentences on the pattern you see across them.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 295,822 | 8,085 | 265.2 | 24,652 | 674 | 22.1 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 293,480 | 7,262 | 466.2 | 24,457 | 605 | 38.8 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 292,426 | 8,167 | 246.7 | 24,369 | 681 | 20.6 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 295,058 | 7,934 | 246.2 | 24,588 | 661 | 20.5 |
| traces/own-own-rerank.jsonl | rerank | 34 | 34 | 2 | 871,257 | 10,300 | 345.0 | 25,625 | 303 | 10.1 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 401,014 | 8,633 | 277.3 | 20,051 | 432 | 13.9 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 383,015 | 8,766 | 276.6 | 19,151 | 438 | 13.8 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 383,653 | 9,377 | 293.1 | 19,183 | 469 | 14.7 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 393,524 | 9,108 | 280.3 | 19,676 | 455 | 14.0 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 738,469 | 17,338 | 529.7 | 18,462 | 433 | 13.2 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.243 | [-0.476, -0.010] | 20,051 | 13.9 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.188 | [-0.392, +0.017] | 20,051 | 13.9 | not distinguishable |
| shared practice: hybrid minus rerank | 20 | -0.279 | [-0.443, -0.128] | 20,051 | 13.9 | rerank higher |
| own: bm25 minus rerank | 34 | -0.367 | [-0.509, -0.226] | 25,625 | 10.1 | rerank higher |
| own: dense minus rerank | 34 | -0.229 | [-0.373, -0.093] | 25,625 | 10.1 | rerank higher |
| own: hybrid minus rerank | 34 | -0.270 | [-0.407, -0.141] | 25,625 | 10.1 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-bm25_lab.jsonl | bm25_lab | 34 | 0.03 | 0.8 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 34 | 0.03 | 0.9 |
| traces/retrieval/own-own-dense.jsonl | dense | 34 | 0.12 | 3.7 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 34 | 0.17 | 4.9 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.04 | 1.9 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.14 | 6.8 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.19 | 9.5 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.08 | 2.0 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.23 | 5.9 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.37 | 9.4 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.725 | 0.750 | 0.727 |
| rerank.r2 | 0.725 | 0.750 | 0.727 |
| rerank.r3 | 0.725 | 0.750 | 0.731 |
| range (max minus min) | 0.000 | 0.000 | 0.004 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.108 | [+0.025, +0.209] | rerank.r1 higher |
| rerank.r2 minus hybrid | Recall@10 | +0.108 | [+0.025, +0.209] | rerank.r2 higher |
| rerank.r3 minus hybrid | Recall@10 | +0.108 | [+0.025, +0.209] | rerank.r3 higher |
| rerank.r1 minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.279 | [+0.128, +0.443] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.270 | [+0.156, +0.392] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.270 | [+0.156, +0.392] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.274 | [+0.159, +0.396] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
