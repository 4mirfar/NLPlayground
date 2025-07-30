# Text Preprocessing

This section we learn about text preprocessing, including normalization etc.

## What is Text?

- Characters (e.g., a, b, 1, !)
- Words
- Phrases and name entities
- Sentences
- Paragraphs

## Tokenization

Tokenization is the process of splitting input into smaller parts called tokens.

## What is a Word? Where is the Word Boundary?

- A word is a meaningful sequence of characters.
- Key question: How do we find word boundaries?

- Word boundaries vary across languages.
- In English and Persian, spaces and punctuation often help.
  - Example: spaces ( ), commas (,), periods (.)


## Common Word Forms

- There are two common definitions for a word:

### Word Type (Type)
- The **unique** entries in the vocabulary (e.g., how many distinct words exist?).

### Word Token (Token)
- The actual occurrences of those words (e.g., how many total words appear? even repeated ones).


## Example: Tokens vs. Types

Sentence:
They lay back on the San Francisco grass and looked at the stars and their

- How many tokens? → 14 or 15?
- How many types (unique words)? → 11, 12, or 13?


## Tokens and Types in Real Datasets

| Dataset                        | Tokens         | Types (Vocabulary) |
|-------------------------------|----------------|---------------------|
| Switchboard phone conversations | 2.4 million    | 20,000              |
| Shakespeare                    | 884,000        | 31,000              |
| Google N-grams                 | 1 trillion     | 13 million          |

- N = number of tokens  
- V = set of unique word types  
- |V| = vocabulary size

📌 Church and Gale (1990):  
Vocabulary size grows slower than number of tokens:  
**|V| > O(√N)**


## **Important**: Should We Treat Punctuation as Separate Tokens?

- It depends on the task and use case.

- In tasks like sentiment analysis, punctuation (like "!" or "?") can be important.

Example:
“I hate dogs.”  
“I hate dogs?”

→ These two sentences have different meanings.

→ In tokenization, punctuation may be kept:
["I", "hate", "dogs", "?"]

⚠️ Some libraries like `CountVectorizer` in scikit-learn remove punctuation by default during tokenization.

## Character-Based Tokenization (Simple)

Instead of breaking text into words, we can break it into characters.

Example:
"dog" → ["d", "o", "g"]

### Why do this?

✅ Pros:
- We don’t need to save a big word list.
- It helps when we see new or weird words.
- It works well in deep learning models.

❌ Cons:
- Each word becomes many tokens → longer input.
- Characters don’t have much meaning alone.
- It’s harder for the model to learn from long sequences of characters.

## Slide 18 – Character vs. Word Tokens

✅ Word tokens have more meaning.

Example: The word "کبوتر" (pigeon) gives a clear image or meaning.

❌ Character tokens have less meaning.

Example: The character "d" appears in "dog", "door", and "duck" — but on its own, it doesn’t mean much.

→ So, word-based tokens are usually more meaningful than character-based ones.

## Slide 19 – Why Use Character Tokens?

✅ Number of characters is small.
- English has only 26 letters + some punctuation.

✅ Vocabulary made of characters is very small.
- Easier to store and process.

✅ Computers can handle character-based data more easily and with less memory.

## Slide 20 – Subword Tokenization

Subword tokens are **parts of words**.

Example:
- "eating" → ["eat", "ing"]

Why this helps:
- "eat" and "eating" are similar in meaning.
- If we use subword tokens, the model learns they are related.
- If not, it sees them as totally different words.

→ Better for machine learning models to represent similar words together.

## Slide 21 – Why Subword Tokenization Matters

If two words like "walk" and "walking" are split into subwords, the model learns they are related.

If not, it may treat them as completely different.

📌 Important question:
Should "walk", "walking", "walked", and "walks" all be learned separately?
Or should the model learn their shared meaning?

→ Deep learning models (like Transformers) help answer this with better word representation.

## Slide 22 – Final Note on Tokenization

- Natural language has **lots of exceptions**.
- Tokenization is hard to model with fixed rules.

That’s why:
- Traditional rule-based methods can’t handle all cases.
- We use machine learning to **learn** tokenization from real data.

📌 ML is needed because languages are full of messy exceptions.
