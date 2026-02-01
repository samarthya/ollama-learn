import ollama
import sys
import time

# --- LEVEL 1: THE ORACLE ---
# Goal: Connect to the Large Language Model (LLM) and receive a prophecy (generation).

# --- CONCEPT: THE CLIENT ---
# We use a client to talk to the inference engine (Ollama).
# The engine is stateless: it doesn't remember previous questions unless we send the history back.
try:
    # Attempting to connect to localhost. 
    # If on WSL and Ollama is on Windows Host, ensure Ollama is listening on 0.0.0.0 or use host.docker.internal
    host = 'http://localhost:11434'
    client = ollama.Client(host=host)
    # Test connection by listing models
    client.list()
except Exception:
    print(f"⚠️  Localhost failed. Trying Windows Host IP (172.22.112.1)...")
    try:
        host = 'http://172.22.112.1:11434'
        client = ollama.Client(host=host)
        client.list()
        print(f"✅ Connected to {host}")
    except Exception as e:
        print(f"❌ Failed to summon the Oracle even at {host}: {e}")
        print("💡 TIP: On Windows, run `set OLLAMA_HOST=0.0.0.0` and restart Ollama.")
        sys.exit(1)

# --- CONFIGURATION ---
model_name = "mistral" # Or "llama3", make sure you have pulled it: `ollama pull mistral`
prompt = "Explain why the sky is blue in one sentence."

print(f"🔮 Summoning {model_name}...")
print(f"❓ Question: {prompt}\n")
print("💬 The Oracle speaks:")

# --- CONCEPT: STREAMING ---
# LLMs generate text token by token (like a typewriter).
# Streaming lets us see the answer as it's being "thought" of.
try:
    stream = client.generate(model=model_name, prompt=prompt, stream=True)
    
    start_time = time.time()
    for chunk in stream:
        # Each chunk contains a 'response' field with the next token
        print(chunk['response'], end='', flush=True)
    print("\n")
    
    end_time = time.time()
    print(f"\n⚡ Insight received in {end_time - start_time:.2f} seconds.")

except Exception as e:
    print(f"\n❌ The Oracle is silent. Error: {e}")
    print("Tip: Make sure Ollama is running and the model is pulled (e.g., 'ollama pull mistral')")
