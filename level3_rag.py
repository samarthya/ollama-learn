import ollama
import numpy as np
import sys

# --- LEVEL 3: THE WEAVER ---
# Goal: Build a RAG system (Retrieval Augmented Generation).
# We will "augment" the LLM's knowledge with our own private data.

# --- CONFIGURATION ---
HOST = 'http://172.22.112.1:11434'
MODEL = "mistral"

try:
    client = ollama.Client(host=HOST)
except Exception as e:
    sys.exit(1)

# --- THE KNOWLEDGE BASE ---
# Normally this would be a database (like we simulated in Level 2).
# Here is our "Secret Knowledge" that the LLM definitely doesn't know.
knowledge_base = [
    "The secret password to the Guild is 'BlueLotus'.",
    "The Guild Master's favorite food is Spicy Ramen, not Sushi.",
    "To open the magic door, you must knock three times and whistle.",
    "The ancient dragon sleeps in the Cavern of Echoes, under the Gray Mountain."
]

print("📚 Indexing Knowledge Base...")
vector_store = []
for sentence in knowledge_base:
    # Embed every sentence (Turn it into numbers)
    emb = client.embeddings(model=MODEL, prompt=sentence)['embedding']
    vector_store.append({"text": sentence, "vector": emb})

# --- UTILITY: COSINE SIMILARITY ---
def cosine_similarity(v1, v2):
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# --- THE RAG LOOP ---
def retrieve(question):
    print(f"🕵️  Searching for answers to: '{question}'")
    # 1. Embed the question
    question_emb = client.embeddings(model=MODEL, prompt=question)['embedding']
    
    # 2. Find the closest match in our store
    best_match = None
    highest_score = -1
    
    for item in vector_store:
        score = cosine_similarity(question_emb, item['vector'])
        if score > highest_score:
            highest_score = score
            best_match = item['text']
            
    print(f"📖 Found relevant info (Score: {highest_score:.4f}): \"{best_match}\"")
    return best_match

def generate_with_rag(question):
    # 1. RETRIEVE
    context = retrieve(question)
    
    # 2. AUGMENT (Context Injection)
    # We construct a special prompt telling the LLM to use the context.
    final_prompt = f"""
    You are a helpful assistant. Answer the question based ONLY on the following context.
    
    Context: {context}
    
    Question: {question}
    """
    
    print("🔮 Weaving the spell (Generating)...")
    # 3. GENERATE
    response = client.generate(model=MODEL, prompt=final_prompt, stream=False)
    return response['response']

# --- THE QUEST ---
questions = [
    "What is the Guild Master's favorite food?",
    "How do I open the magic door?",
    "Where is the dragon?"
]

print("\n--- STARTING EXECUTION ---\n")
for q in questions:
    answer = generate_with_rag(q)
    print(f"💬 Answer: {answer}\n" + "-"*40 + "\n")
