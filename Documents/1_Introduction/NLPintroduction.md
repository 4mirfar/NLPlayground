wh# NLP Pyramid

The image below is a Natural Language Processing (NLP) Pyramid, a conceptual diagram showing the layered structure of how language is understood and processed by machines. Each layer builds upon the one below it — from raw forms to higher meaning.

![alt text](imgs/image.png)


### 🧱 1. **Morphology** – Word Pieces

💬 *What are the parts of a word?*

* Example: **“unhappiness”** = un + happy + ness
* Think: cutting words into useful pieces.


### 🧱 2. **Syntax** – Sentence Structure

💬 *How are words arranged?*

* Example: **“The dog runs.”** is correct, but **“Dog the runs”** is weird.
* Think: grammar rules.


### 🧱 3. **Semantics** – Word Meaning

💬 *What do the words mean?*

* Example: **“Bank”** – is it for money or a river?
* Think: understanding the *real meaning* of words.

### 🧱 4. **Pragmatics** – Real-Life Meaning

💬 *What do you actually mean?*

* Example: You say, **“Can you pass the salt?”** — you're not asking about ability, you're politely asking for salt.
* Think: tone, context, intention.

### 🚀 So how does NLP work?

It starts with breaking down words (morphology),
figures out sentence structure (syntax),
understands meaning (semantics),
and finally gets your *real* point (pragmatics).


# ❓ Why is NLP hard?

1. **Different grammar rules** are used by different people — even in the same language.
2. **High grammar flexibility** — natural languages are messy, full of exceptions and odd structures.
3. **People skip punctuation**, making it harder for machines to understand sentences.
4. **Same sentence can mean different things** depending on how you read it.

---

### 🧠 Example:

> **"At last a computer that understands you like your mother"**

This sentence is **grammatically correct**, but its **meaning is unclear**. It could mean:

1. The computer understands you **as well as your mother understands you**.
2. The computer understands that **you like your mother**.
3. The computer understands you **just as it understands your mother**.

---

## 🔊 Ambiguity at the **Acoustic Level**

Sometimes the confusion starts even earlier — during **speech recognition**!

When someone says:

> "... a computer that understand you lie cured mother"

The system might "hear" and report one of two things:

1. **"... you like your mother"**
2. **"... you lie, cured mother"**

Why? Because **"like your"** and **"lie cured"** sound similar when spoken quickly.
Even though both options are **grammatically valid** in English, only one is correct — and speech recognizers may choose the wrong one based on sound alone.

### 💡 Why this matters:

Machines don’t *really* know what we mean — unless we give them **lots of context, training, and rules**.
Humans use **emotion, experience, tone, and common sense** — machines don't (yet).


## Slide 49 – Perplexity (Important)

### Definition
Perplexity measures how well a language model predicts a sequence of words.

It answers:
> "On average, how many equally likely choices does the model think it has for the next word?"

---

### Calculation Steps
1. Take a test set (sentences not seen in training).
2. Compute the probability of the whole sequence: P(w1, w2, ..., wN).
3. Normalize by the sequence length (N).
4. Take the inverse of that average probability.

---

### Formula
Perplexity = ( 1 / P(w1, w2, ..., wN) )^(1/N)  

Where:
- **P(w1, ..., wN)** = probability of the sequence
- **N** = number of words

---

### Interpretation
- **Lower perplexity** → Better model (less uncertainty)
- **Higher perplexity** → Worse model (more uncertainty)

---

### Example
If Perplexity = 10:
- The model’s uncertainty is like having 10 equally likely next-word options.
