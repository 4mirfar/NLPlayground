Sure! Here's a step-by-step guide in English on how to use the **Reuters corpus** and build a model using **n-grams**.

---

## 🅰️ a. Preprocessing

1. **Load the Reuters corpus**
   Use the `nltk` library:

   ```python
   import nltk
   from nltk.corpus import reuters
   nltk.download('reuters')
   nltk.download('punkt')  # For tokenization
   ```

2. **Get the documents:**

   ```python
   documents = [reuters.raw(fileid) for fileid in reuters.fileids()]
   ```

3. **Clean the text:**

   * Convert to lowercase
   * Tokenize (split into words)
   * Remove punctuation
   * Remove stopwords (optional)

   ```python
   from nltk.corpus import stopwords
   from nltk.tokenize import word_tokenize
   import string

   nltk.download('stopwords')
   stop_words = set(stopwords.words('english'))

   def preprocess(text):
       text = text.lower()
       tokens = word_tokenize(text)
       tokens = [t for t in tokens if t.isalpha()]  # keep only words
       tokens = [t for t in tokens if t not in stop_words]
       return tokens

   cleaned_docs = [preprocess(doc) for doc in documents]
   ```

---

## 🅱️ b. Building an n-gram Model

1. **Generate n-grams**
   Let's use bigrams (n = 2) as an example:

   ```python
   from nltk import ngrams
   from collections import Counter

   n = 2
   all_ngrams = []

   for tokens in cleaned_docs:
       all_ngrams.extend(ngrams(tokens, n))

   freq_dist = Counter(all_ngrams)
   ```

2. **View the most common n-grams:**

   ```python
   for gram, freq in freq_dist.most_common(10):
       print(f"{gram}: {freq}")
   ```

3. **Create a conditional frequency distribution**
   This shows what words follow a given word:

   ```python
   from nltk.probability import ConditionalFreqDist

   cfd = ConditionalFreqDist()
   for w1, w2 in all_ngrams:
       cfd[w1][w2] += 1

   print(cfd['market'].most_common(5))  # Words that often follow "market"
   ```

---

Would you like to:

* Build a trigram model instead?
* Generate text using this model?
* Visualize the frequencies?

Let me know!
