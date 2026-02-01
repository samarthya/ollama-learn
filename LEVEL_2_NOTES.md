# 📜 Level 2 Grimoire: The Archive

Welcome, Librarian. You have mastered the Oracle (Generation). Now you must master the **Archive (Retrieval)**.

## 🧮 Concept 1: Embeddings ( The Translation)

Computers understand numbers, not concepts.

- To a computer, "Apple" and "Fruit" are just different strings of bytes.
- An **Embedding Model** translates text into a **Vector** (a long list of floats).
- `mistral` (4096 dimensions) or `nomic-embed-text` (768 dimensions).
- **Key Idea**: In this N-dimensional space, similar concepts are physically close to each other.

## 📐 Concept 2: Cosine Similarity (The Compass)
How do we find the "closest" concept?
- We don't use typical distance (Euclidean).
- We use **Cosine Similarity**: The cosine of the angle between two vectors.
- **1.0**: Same direction (Identical meaning).
- **0.0**: 90 degrees (Unrelated).
- **-1.0**: Opposite direction (Opposite meaning).

## 🗄️ Concept 3: Vector Store (The Library)
A Vector Store is a specialized database that:
1.  Takes your text.
2.  Turns it into embeddings.
3.  Indexes them for fast lookup using similarity math.
(We simulated a tiny in-memory one in `level2_librarian.py` using a Python dictionary).

---

**Next Level Info:**

Now that we can **Generate** (Level 1) and **Retrieve** (Level 2), we will combine them.
In Level 3, we become **Weavers** and build **RAG** (Retrieval Augmented Generation).
