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

