# 🗺️ The RAG Architect's Journey: A Retrospective

We began with a simple script and ended with a reasoning agent. Here is the story of how our AI evolved, level by level.

## 🟢 Level 1: The Awakening (The Oracle)

**"The Brain in a Jar"**

- **The Problem**: We had a powerful AI (`mistral`), but it was just a text completion engine. It had no memory of us and no knowledge of the outside world.
- **The Solution**: We built a basic client (`level1_oracle.py`).
- **Complexity Added**: **Connectivity**. We established the link between Python and the LLM.
- **Key Concept**: *Statelessness* (The Oracle forgets you immediately).

## 🔵 Level 2: The Translation (The Librarian)

**"Teaching Math to Poets"**

- **The Problem**: We wanted to search for information, but keyword search ("Dragon") fails if the text says "The great winged beast".
- **The Solution**: We accepted that "Meaning" = "Numbers". We built an Embedding script (`level2_librarian.py`).
- **Complexity Added**: **Semantic Understanding**. We moved from matching words to matching *concepts* (Vectors).
- **Key Concept**: *Cosine Similarity* (The geometry of meaning).

## 🟣 Level 3: The Weaver (Simple RAG)

**"The Open Book Exam"**

- **The Problem**: The Oracle hallucinated answers. It didn't know our secrets ("BlueLotus").
- **The Solution**: We fed the relevant pages (from Level 2) directly into the Oracle's prompt (`level3_rag.py`).
- **Complexity Added**: **Context Injection**. We learned to manipulate the model's short-term memory (Context Window).
- **Key Concept**: *RAG Loop* (Retrieve -> Augment -> Generate).

## 🟠 Level 4: The Critic (Evaluation)

**"The Conscience"**

- **The Problem**: The Weaver was too eager. If we asked about "Dragons", it found "Ramen" and tried to answer anyway.
- **The Solution**: We added a "Judge" step. Before answering, the model critiques its own retrieved evidence (`level4_critic.py`).
- **Complexity Added**: **Self-Reflection**. The system can now say "I don't know" instead of lying.
- **Key Concept**: *Grounding* (Verifying the source).

## 🔴 Level 5: The Automaton (Agents)

**"The Hands"**

- **The Problem**: RAG only looks at the *past* (static text). It can't calculate `25 * 45` or check live data.
- **The Solution**: We gave the model **Tools** (Python functions). The model decides *when* to use them (`level5_agent.py`).
- **Complexity Added**: **Agency**. The model moved from "Reading" to "reasoning and Acting".
- **Key Concept**: *Tool/Function Calling*.

## 🟡 Level 6: The Mirror (UI)

**"The Visualizer"**

- **The Problem**: A terminal is scary. We can't "see" what the tools or the critic are doing.
- **The Solution**: We built a **Streamlit** app (`level6_app.py`).
- **Complexity Added**: **State Management**. We had to manage chat history and `st.session_state`.
- **Key Concept**: *Visualizing Thought* (Showing the tool calls in real-time).

## ⚪ Level 7: The Capsule (Containers)

**"The Space Suit"**

- **The Problem**: It works on my machine, but will it work on yours?
- **The Solution**: We packaged it all into a **Docker Container** (`Dockerfile`).
- **Complexity Added**: **Networking**. Connecting a container back to the host machine's Ollama.
- **Key Concept**: *Infrastructure as Code*.

---

# 🚀 How to Run the App (The Exhibition)

You can run the full "RAG Architect's Mirror" using Docker or Podman.

### Option 1: Docker

```bash
docker-compose up --build
```

### Option 2: Podman (Rootless)

```bash
podman-compose up --build
# Or with newer podman versions:
podman compose up --build
```

### Option 3: Python (Local)

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run level6_app.py
```

Access the app at: `http://localhost:8501`

---

# 🔮 What's Next? (Advanced RAG)

- **Goal**: Fix the "Dragon vs Ramen" embedding issue definitively.
- **Tech**:
    - Use a *real* embedding model (e.g., `nomic-embed-text`).
    - **Hybrid Search**: Combine Keywords (BM25) + Vectors.
    - **Reranking**: A second pass to sort results better.
