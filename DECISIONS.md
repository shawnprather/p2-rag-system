# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?

I picked the godot game engine documentation in stage two because I've been working on making a game and it has been somewhat difficult to find good documentation for the issues I've been running into. So I wanted to make a rag for it so I could search for the important information I need to get to help me make the game.

Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

I think bm25 will do the worst by far purely since my prompts were wrote in plain english and mainly paraphases which bm25 doesn't do that good at. In comparison I think rerank will be by far the best since it is the most expensive and slowest and has the most steps to be able to get the right result espiecally the end sorting.

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

One real design choice that could have gone either way is the bm25 tokenizer when I was testing codes vs lab. I decided to stick with codes after doing my ablation since the results were very slightly better than lab (nDCG@10 for codes was 0.572 and 0.555 for lab). I think there would be some prompts where lab would do better than codes but given the documentation base where _,-, and other symbols have a fair bit of meaning I found it valuable to keep.c

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

I had to take a fair bit of time to decide on which corpus to choose since Claude was trying to push me towards doing a mineral or mining corpus which is interesting but isn't the most useful to me. After having it help me brainstorm ideas for stuff that might be relevant I realized that having a rag for the Godot game engine would be helpful since I have been recently learning to make games within Godot. So I picked Godot 4.7 doc since that is the version I am using and it will be of help to me.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

One number I don't fully trust is the Wilson intervals for the verified questions since there was only 8 questions which it was 100% on but that really wasn't enough data to be able to come to a good basis since that mens that it is between 68% and 100% actual. To trust it I would need to test more questions to confirm it is 100%. I did do some stuff to test it being the 3 repeat tests indirectly which they also all got 8/8 which means it is consistent at least.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

Some stuff that is wrong or I would redo is that the first stage for rerank dropped a fair few good results so incraesing the number of candidates up to 40 would most likley help a bunch (query c10 in runs/own/hybrid.trec relevant page io-saving_games is ranked #27 outside candidates). Also being able to actually include the coding API would also be useful but I don't know how much help it would be since it is very verbose and not that explanitive (the classes/ folder of the godot-docs repo). A bunch of the docs also repeat their own title as the first line (for example corpora/own/docs/physics-using_character_body_2d.md) and all of the images were lost which would be good to have been saved.

