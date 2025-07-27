import math
from collections import defaultdict, Counter

# Assume you already have this from your preprocessing
def build_ngram_model(tokenized_sentences, n):
    model = defaultdict(Counter)
    for sentence in tokenized_sentences:
        padded = ['<s>'] * (n-1) + sentence + ['</s>']
        for i in range(len(padded) - n + 1):
            context = tuple(padded[i:i+n-1])
            word = padded[i+n-1]
            model[context][word] += 1
    return model

# Convert counts to probabilities
def get_prob(model, context, word, vocab_size, smoothing=1):
    context_count = sum(model[context].values())
    word_count = model[context][word]
    return (word_count + smoothing) / (context_count + smoothing * vocab_size)

# Perplexity calculation
def calculate_perplexity(model, test_sentences, n, vocab):
    vocab_size = len(vocab)
    log_prob_sum = 0
    word_count = 0
    for sentence in test_sentences:
        padded = ['<s>'] * (n-1) + sentence + ['</s>']
        for i in range(len(padded) - n + 1):
            context = tuple(padded[i:i+n-1])
            word = padded[i+n-1]
            prob = get_prob(model, context, word, vocab_size)
            log_prob_sum += -math.log(prob)
            word_count += 1
    return math.exp(log_prob_sum / word_count)
