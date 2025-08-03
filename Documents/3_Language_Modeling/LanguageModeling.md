# Language Modeling


## Slide 1 – Language Modeling

📌 Topic: **Language Modeling (LM)**  
- Based on the concept of probability over word sequences.
- Includes: Markov Assumption, N-gram models, Perplexity, and Smoothing.

Presented by: Hamidreza Baradaran Kashani


---


## Slide 2 – Topics in This Section

- What is a Language Model (LM)?
- Markov Assumption
- N-gram probability estimation
- Evaluating LMs (Perplexity)
- Generalization and zero probabilities
- Laplace Smoothing

---


## Slide 3 – Intro to Language Modeling (LM)

Language Modeling means:
- Assigning a **probability** to a sequence of words in a language.

Example use:
- In Machine Translation (MT):
  - P("high winds tonite") > P("large winds tonite")
  → because it's more natural.


---


## Slide 4 – More Uses of Language Models

Language Models help in:

- **Spell Correction**:
  - P("about fifteen minutes from") > P("about fifteen minuets from")

- **Speech Recognition**:
  - P("I saw a van") >> P("eyes awe of an")

- Also useful in QA, summarization, etc.


---

## Slide 5 – What LM Really Does

Goal: Compute probability of a sentence like:

```text
P(W) = P(w1, w2, w3, ..., wn)
````

Using conditional probabilities:

```text
P(w5 | w1, w2, w3, w4)
```

→ This is the base idea of Language Models.



---


## Slide 6 – Example: Sentence Probability

Sentence:  
```text
Its water is so transparent that ...


We want to calculate:

```text
P(its, water, is, so, transparent, that)
```

How?
→ Use **Chain Rule of Probability**

````

---

## Slide 7 – Chain Rule Formula

To calculate:

```text
P(its water is so transparent)
````

We use:

```text
P(its) ×
P(water | its) ×
P(is | its, water) ×
P(so | its, water, is) ×
P(transparent | its, water, is, so)
```

This method is exact, but can be complex without simplification.


## Summary: Language Modeling (Slides 8–21)

- We want to compute the probability of a sentence:
  P(w1, w2, ..., wn)

- We use the **chain rule** to break it down:
  P(w1) × P(w2 | w1) × P(w3 | w1, w2) ...

- This gives accurate results but is **computationally expensive**.

- Why? Because there are too many word combinations to count.

- So we simplify using the **Markov assumption**:
  Only look at a few previous words (not all of them).

- **Unigram model**:
  Each word is independent:  
  P(w1, w2, ...) = P(w1) × P(w2) × ...

- Unigram output sounds random:
  “fifth an of futures the an ...”

- **Bigram model**:
  P(wi | wi-1), uses 1 previous word.

- Bigram output has more structure:
  “texaco rose one in this issue is ...”

- **Trigram model**:
  P(wi | wi-2, wi-1), uses 2 previous words.

- These are called **N-gram models** (N = 1, 2, 3, ...)

- Higher N means more context but also more data needed.

- We estimate probabilities using counts:
  P(w2 | w1) = Count(w1, w2) / Count(w1)

- Example:
  P("am" | "I") = Count("I am") / Count("I")

- N-gram models are trained by counting word sequences from real data.

- Used in many NLP tasks like translation, speech recognition, and autocomplete.

## Slide 22 – N-gram Probability (General Formula)

P(w1, w2, ..., wn) ≈  
P(w1) × P(w2 | w1) × P(w3 | w1, w2) × ... × P(wn | wn-2, wn-1)

⬇️ In trigram form (3-gram):

P(wi | wi−2, wi−1) = Count(wi−2, wi−1, wi) / Count(wi−2, wi−1)

## Summary – Slides 23 to 30: Start/End Tokens & N-gram Probability

1. Use `<s>` to mark the start of a sentence, and `</s>` for the end.

2. In bigram models:
   - P("first word" | `<s>`)
   - P(`</s>` | "last word")

3. In trigram models:
   - Add two start tokens: `<s> <s> I am Sam </s>`

4. These tokens help handle:
   - The beginning of a sentence (provides context)
   - The end of a sentence (tells the model when to stop)

5. Without `</s>`, the model may keep generating words forever.

6. N-gram sentence probability:
   - P(w1, w2, ..., wn) ≈  
     P(w1|<s>) × P(w2|w1) × ... × P(</s>|wn)

7. Probabilities are calculated using counts from real data:
   - P(wi | wi-1) = Count(wi-1, wi) / Count(wi-1)

8. Final sentence probability is the product of all N-gram probabilities.

## Slide 32 – Count Matrix

- Create a **matrix of counts** for all bigrams in the corpus.
- Rows = previous word, columns = next word.
- Each cell contains the number of times that bigram occurred in the training data.

## Slide 33 – Probability Matrix

- Convert the count matrix into a **probability matrix**.
- Formula:
  P(next_word | previous_word) = Count(previous_word, next_word) / Count(previous_word)
- Each row in the probability matrix sums to 1.

## Slide 34 – Language Model

- The probability matrix becomes the **language model**.
- This model can:
  - Calculate the probability of a sentence.
  - Generate new sentences based on learned probabilities.

## Slide 35 – Example Sentences

Example dialogue-related sentences for training:
- can you tell me about any good cantonese restaurants close by
- mid priced thai food is what i’m looking for
- tell me about chez panisse
- can you give me a listing of the kinds of food that are available
- i’m looking for a good place to eat breakfast
- when is caffe venezia open during the day

![alt text](imgs/photo_1.png)

## Slide 43 – Evaluating a Language Model

- We want to know: How good is our LM?
- A good LM:
  - Gives higher probabilities to more common/realistic sentences.
  - Gives lower probabilities to rare/incorrect sentences.
- It should reflect both grammatical correctness and common usage.

## Slide 44 – Evaluation Process

- Train the LM on a **training set**.
- Test it on a **different test set** that the model hasn’t seen.
- Use an **evaluation metric** to measure how well the LM predicts the test set.

## Slide 45 – Why Separate Data?

- The training set is for learning parameters.
- The test set is for checking performance.
- The test set must be different to avoid overfitting.
- The evaluation metric tells us how good the LM is on unseen data.

## Slide 46 – Extrinsic Evaluation

- Measure LM performance inside a **real application**.
- Examples:
  - Spell correction → % of correctly fixed words.
  - Machine translation → % of correct translations.
  - Speech recognition → Word Error Rate (WER).
- Compare two LMs (A vs. B) in the same task.

## Slide 47 – Problems with Extrinsic Evaluation

- Time-consuming and expensive.
- Not always practical for every task.
- Suggested alternative: **Intrinsic Evaluation** (e.g., perplexity).
- Intrinsic evaluation is faster, but only works well if the test data is very similar to the training data.

## Slide 48 – Shannon Game

- A simple way to measure LM quality:
  - Hide the next word and ask the model (or a human) to guess it.
- Unigram models perform poorly at this game.
- N-gram models do better because they use context.
