import ollama
import numpy as np
import sys

# --- LEVEL 4: THE CRITIC ---
# Goal: Stop the LLM from answering if the retrieved context is hallucinated or irrelevant.
# We add a "Judge" step before the final generation.

# --- CONFIGURATION ---
HOST = 'http://172.22.112.1:11434'
MODEL = "mistral"

try:
    client = ollama.Client(host=HOST)
except Exception as e:
    sys.exit(1)

# --- REUSING KNOWLEDGE BASE (Same as Level 3) ---
knowledge_base = [
    "The secret password to the Guild is 'BlueLotus'.",
    "The Guild Master's favorite food is Spicy Ramen, not Sushi.",
    "To open the magic door, you must knock three times and whistle.",
    "The ancient dragon sleeps in the Cavern of Echoes, under the Gray Mountain."
]
vector_store = []
for sentence in knowledge_base:
    emb = client.embeddings(model=MODEL, prompt=sentence)['embedding']
    vector_store.append({"text": sentence, "vector": emb})

def cosine_similarity(v1, v2):
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def retrieve(question):
    question_emb = client.embeddings(model=MODEL, prompt=question)['embedding']
    best_match = None
    highest_score = -1
    for item in vector_store:
        score = cosine_similarity(question_emb, item['vector'])
        if score > highest_score:
            highest_score = score
            best_match = item['text']
    return best_match, highest_score

# --- NEW: THE JUDGE ---
def judge_context(question, context):
    print("⚖️  The Judge is evaluating the evidence...")
    # We ask the LLM specifically to grade the relevance.
    judge_prompt = f"""
    You are a strict judge. 
    Does the following Context contain the answer to the Question?
    Respond ONLY with "YES" or "NO".
    
    Context: {context}
    Question: {question}
    
    Verdict:
    """
    response = client.generate(model=MODEL, prompt=judge_prompt, stream=False)
    verdict = response['response'].strip().upper()
    return "YES" in verdict

# --- THE SAFE RAG LOOP ---
def generate_safe_rag(question):
    print(f"\n❓ Asking: '{question}'")
    
    # 1. RETRIEVE
    context, score = retrieve(question)
    print(f"📖 Retrieved (Score: {score:.4f}): \"{context}\"")
    
    # 2. EVALUATE (The Critic)
    is_relevant = judge_context(question, context)
    
    if not is_relevant:
        print("❌ CRITIC: The retrieved context is irrelevant. Aborting generation.")
        return "I do not have enough information to answer that."
    
    print("✅ CRITIC: Evidence accepted.")
    
    # 3. GENERATE (The Weaver)
    final_prompt = f"""
    Answer the question based ONLY on the context.
    Context: {context}
    Question: {question}
    """
    response = client.generate(model=MODEL, prompt=final_prompt, stream=False)
    return response['response']

# --- THE TRIALS ---
questions = [
    "What is the Guild Master's favorite food?",
    "Where is the dragon?",
    "What is the capital of France?" # Completely unknown
]

for q in questions:
    answer = generate_safe_rag(q)
    print(f"💬 Answer: {answer}\n" + "-"*40)
