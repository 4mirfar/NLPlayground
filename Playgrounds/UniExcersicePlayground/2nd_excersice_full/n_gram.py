import nltk
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
from nltk.probability import ConditionalFreqDist
from collections import Counter
# import string

# Download required resources
nltk.download('reuters')
nltk.download('punkt')
nltk.download('stopwords')

# Load documents
documents = [reuters.raw(fileid) for fileid in reuters.fileids()]

# Preprocessing function
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

# Apply preprocessing
cleaned_docs = [preprocess(doc) for doc in documents]

# Build n-grams (example: bigram)
n = 2
all_ngrams = []

for tokens in cleaned_docs:
    all_ngrams.extend(ngrams(tokens, n))

# Frequency distribution
freq_dist = Counter(all_ngrams)

# Print top 10 most common n-grams
for gram, freq in freq_dist.most_common(10):
    print(f"{gram}: {freq}")

# Conditional Frequency Distribution
cfd = ConditionalFreqDist()
for w1, w2 in all_ngrams:
    cfd[w1][w2] += 1

# Example: words that follow "market"
print("\nWords following 'market':")
print(cfd['market'].most_common(5))
