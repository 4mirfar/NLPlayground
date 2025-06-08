import random
from collections import defaultdict

# Example trained N-gram model: trigram_model[(w1, w2)] = [w3_1, w3_2, ...]
# Assume this model is already trained using the Reuters corpus
trigram_model = defaultdict(list)

# Example dummy data — in practice this should come from your trained model
sample_sentences = [
    "the stock market",
    "stock market rose",
    "market rose sharply",
    "rose sharply today",
    "sharply today after",
    "today after news",
    "after news about",
    "news about earnings"
]

# Build the trigram model from the sample data
for sentence in sample_sentences:
    words = sentence.split()
    for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        trigram_model[key].append(words[i+2])

# Function to generate text from trigram model
def generate_text(model, start_words, num_words=20):
    output = list(start_words)
    for _ in range(num_words):
        prefix = tuple(output[-2:])
        if prefix in model:
            next_word = random.choice(model[prefix])
            output.append(next_word)
        else:
            break
    return ' '.join(output)

# Start generation from a bigram (w1, w2)
start = ("the", "stock")
generated_text = generate_text(trigram_model, start_words=start, num_words=15)
print("Generated Text:")
print(generated_text)
