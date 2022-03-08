# NLP-ContextAnalysisPpmi-PairSimilarities


PART1:

Computing the Positive Pointwise Mutual Information (PPMI) of pairs [word, context-word]. The 
context of a word is the “window” of words consisting of (i) 5 words to the left of 
the word; and (ii) 5 words to the right of the word. If there are fewer then 5 
words to the right or the left of the word in the same sentence, the context will 
be padded with “NIL”. Computing the PPMI for:
a. The word “chairman” for the context-word “said”;
b. The word “chairman” in the context-word “of”;
c. The word “company” in the context-word “board”;
d. The word “company” in the context-word “said”.


PART2:

Finding which words are more similar among: [chairman, company], [company, 
sales] or [company, economy] when considering only the contexts which contain 
words “said”, “of”, and “board”
