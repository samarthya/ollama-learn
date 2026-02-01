import ollama
import numpy as np
import sys

# --- LEVEL 2: THE LIBRARIAN ---
# Goal: Understand Embeddings and Vector Search.

# --- CONFIGURATION ---
# Using the Windows Host IP as discovered in Level 1
HOST = 'http://172.22.112.1:11434'
MODEL = "mistral"

try:
    client = ollama.Client(host=HOST)
    client.list() # Test connection
    print(f"📚 Librarian is ready at {HOST}")
except Exception as e:
    print(f"❌ Librarian cannot reach the Archive: {e}")
    sys.exit(1)

# --- CONCEPT: EMBEDDINGS ---
# An embedding is a list of numbers (vector) that represents the *meaning* of text.
# Words with similar meanings will have similar numbers.

def get_embedding(text):
    print(f"🧮 Translating '{text}' into numbers...")
    # Ollama provides an endpoint to get embeddings from a model
    response = client.embeddings(model=MODEL, prompt=text)
    return response['embedding']

# 1. Let's get some vectors
words = ["Apple", "Fruit", "Dog", "Car"]
vectors = {}

for w in words:
    vectors[w] = get_embedding(w)
    # Print the first 5 dimensions just to see them
    print(f"   Shape: {len(vectors[w])} dimensions. First 5: {vectors[w][:5]}...")

# --- CONCEPT: COSINE SIMILARITY ---
# How do we check if two vectors are similar? We measure the angle between them.
# Similarity = 1.0 (Identical) -> 0.0 (Unrelated) -> -1.0 (Opposite)
# Formula: (A . B) / (||A|| * ||B||)

def cosine_similarity(v1, v2):
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print("\n🔍 Comparing Meanings:")

comparisons = [
    ("Apple", "Fruit"),
    ("Apple", "Dog"),
    ("Apple", "Car"),
    ("Dog", "Car") # Maybe slightly related? Both move?
]

for w1, w2 in comparisons:
    sim = cosine_similarity(vectors[w1], vectors[w2])
    print(f"   Similarity between '{w1}' and '{w2}': {sim:.4f}")

print("\n✨ Insight:")
print("Notice how 'Apple' is closer to 'Fruit' (higher number) than to 'Dog'.")
print("This is how we perform 'Semantic Search'!")
