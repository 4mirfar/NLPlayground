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

## Slide 23 – Stopwords

**Stopwords** are very common words that appear a lot in text but don’t carry much meaning.

Examples:

- English: “the”, “and”, “or”, “is”, “it”
- Persian: "و", "در", "یا", "آن"

🟡 They are usually:
- Pronouns, prepositions, conjunctions, helper verbs, etc.

🛠 No universal list of stopwords exists — each tool may have its own.

## Slide 24 – Why Remove Stopwords?

✅ Useful in many cases:

- Helps reduce the size of the text
- Makes important words stand out more
- Improves accuracy for tasks like text classification

⚠️ But not always good to remove:

- Some stopwords may be important depending on the task

## Slide 25 – When Removing Stopwords is Bad

❌ In tasks like:

- **Machine translation**: stopwords need to be translated
- **Question answering**: removing them might change meaning
- **Text summarization**: affects grammar and structure

Example:

Original: “The movie was **not good** at all”  
After removing stopwords: “movie good”

→ Meaning is completely changed!

## Slide 26 – Libraries with Stopword Lists

Popular NLP libraries that provide stopword lists:

- **NLTK**
- **spaCy**
- **Gensim**
- **Scikit-learn**

⚠️ Be careful: Removing stopwords blindly can change meaning!


## Important: Word Nomalizati0on and Stemming (27)

**Text normalization** = Converting words into a standard form.

Why? Because the same word can appear in many different ways:

Examples:
- "labeled" vs. "labelled"
- "extra-linguistic" vs. "extralinguistic"

→ Normalize them to a single standard form.

## Slide 28 – What is Normalization?

Make all forms of a word the same.

Example:  
"USA" = "U.S.A" → should be treated as the same.

Also:
- "window" and "windows" → both should map to "window" in some tasks.

This helps in:
- Searching
- Matching
- Indexing

## Slide 29 – Case Normalization

Often we convert **all letters to lowercase** for consistency.

Examples:
- "USA" vs. "us"
- "Fed" vs. "fed"
- "SAIL" vs. "sail"

⚠️ But case matters in some tasks like:
- Sentiment analysis
- Information extraction
- Machine translation

## Slide 30 – Morphology & Word Structure

Some words are made of smaller parts (called **morphemes**):

- **Stem**: the core meaning part of a word
- **Affix**: the extra parts (prefixes/suffixes)

Example:
- In "unhappiness":  
  - "happy" = stem  
  - "un" and "ness" = affixes

→ Understanding word structure helps in better normalization.

## Slide 31 – What is Stemming?

**Stemming** = Cutting a word down to its root (stem).

- The goal is to remove suffixes (like -ed, -ing, -s, etc.)
- This helps group similar words.

Examples:
- "automate", "automated", "automatic", "automation"  
  → All become: **automat**

⚠️ Different languages need different stemming rules.

## Slide 32 – How Stemming Works

Stemming = remove or replace word endings (suffixes)

- It’s a simple rule-based process.
- Helps match different forms of a word in search and NLP tasks.

Example:
- "walking" → "walk"
- "plastered" → "plaster"

⚠️ Not always perfect! Sometimes it cuts too much or too little.

## Slide 33 – Porter’s Stemming Algorithm

**Porter Stemmer** is a well-known and simple stemming algorithm for English.

It uses rules to cut word endings step by step.

### Examples:

**Step 1a:**
- "caresses" → "caress"
- "ponies" → "poni"
- "cats" → "cat"

**Step 1b:**
- "walking" → "walk"
- "plastered" → "plaster"

**Step 2 and 3 (longer endings):**
- "relational" → "relate"
- "digitizer" → "digitize"
- "adjustable" → "adjust"

## Slide 34 – Lemmatization

**Lemmatization** = Mapping a word to its **base form** (called lemma or headword)

Examples:
- "am", "are", "is" → "be"
- "cars", "car's", "cars'" → "car"

Sentence:
- "The boy's cars are different colors"  
  → Lemmatized: "the boy car be different color"

🛠 Lemmas are usually looked up in a **dictionary** (not just by rule).


## Slide 35 – Sentence Segmentation

**Sentence segmentation** = Finding where a sentence ends.

Usually we use punctuation like:
- Period `.`
- Question mark `?`
- Exclamation `!`

⚠️ But it's not always clear:
- "Dr." or "U.S.A." use dots but are **not** sentence ends.
- Numbers like "3.4" use dots too.

Solution: Use classifiers (models) to decide:
- Is this the **End of Sentence (EOS)**?
- Or **Not EOS**?

Techniques: Rules, regex, or machine learning.

## Slide 36 – Decision Trees for EOS

We can use a **Decision Tree** to figure out if a word ends a sentence.

Simple idea:
- Is the word at the end of a sentence?
  → Yes or No?

Model checks some features and makes a decision.

## Slide 37 – Features for EOS Decision

Models use features like:

- Word shape after the dot:
  - Does it start with a capital letter?
  - Is it all capital letters? (e.g., "USA")
  - Is it a number?

- Word length (e.g., abbreviations are often short)
- Frequency of seeing that word at sentence end or start

→ These features help classify if the period means a sentence end.

## Slide 38 – ML Models for Sentence Boundary Detection

Some common models used:

- **SVM** (Support Vector Machines)
- **Decision Trees**
- **Logistic Regression**
- **Neural Networks**

Each learns patterns from data to detect where a sentence ends.
