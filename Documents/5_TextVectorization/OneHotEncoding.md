### One-Hot Encoding

**Definition:**  
One-hot encoding is a way to represent words as binary vectors. Each unique word in the vocabulary is assigned a unique index. The word is then represented as a vector of zeros with a single one at the index corresponding to that word.

---

### Example

Suppose we have these two sentences:

```
Sentence 1: this movie is good  
Sentence 2: this movie is bad
```

**Step 1: Build the vocabulary**

```
Vocabulary = [this, movie, is, good, bad]
```

Each word is assigned an index:

```
this  → 1  
movie → 2  
is    → 3  
good  → 4  
bad   → 5
```

**Step 2: Create one-hot vectors**

Each word is represented by a binary vector of length 5 (vocabulary size), with `1` at its index and `0` elsewhere:

```
this  → [1 0 0 0 0]  
movie → [0 1 0 0 0]  
is    → [0 0 1 0 0]  
good  → [0 0 0 1 0]  
bad   → [0 0 0 0 1]
```

**Encoding the sentence `this movie is good`:**

```
[
  [1 0 0 0 0],  // this
  [0 1 0 0 0],  // movie
  [0 0 1 0 0],  // is
  [0 0 0 1 0]   // good
]
```

---

**Notes:**
- Each word is independent; semantic meaning is not captured.
- Vectors are sparse (mostly zeros), which can be inefficient for large vocabularies.
- No similarity is reflected between semantically related words like `good` and `bad`.

