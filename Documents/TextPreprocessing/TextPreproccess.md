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
