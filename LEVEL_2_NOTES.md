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
- **Euclidean Distance**: Measures the straight-line distance between two points. It cares about **magnitude** (length).
    - Example: "Apple" vs "Apple Apple Apple". Euclidean distance is huge (because one vector is longer).
- **Cosine Similarity**: Measures the **angle** between two vectors. It cares about **direction** (topic).
    - Example: "Apple" vs "Apple Apple Apple". Angle is 0. They mean the same thing. 
    - **Why it matters**: In RAG, we want to find content with the same *meaning*, regardless of how long the text is.
- **Formula**: `(A . B) / (||A|| * ||B||)`

## 🔮 Concept 3: The 4096 Dimensions
Your output said: `Shape: 4096 dimensions`.
- Imagine a map with X and Y coordinates (2 dimensions). You can locate any city.
- Now add Altitude (Z) (3 dimensions).
- The "Mistral" model uses **4096 axes** to locate the meaning of a word.
- Each number in `[3.19, -6.00, ...]` is a coordinate on one of those axes.
- **3.19** might represent "Edibility".
- **-6.00** might represent "Mechanical".
(We don't know exactly what each dimension means, but the computer uses them to triangulate meaning).

## 🗄️ Concept 4: Vector Store (The Library)
A Vector Store is a specialized database that:
1.  Takes your text.
2.  Turns it into embeddings.
3.  Indexes them for fast lookup using similarity math.
(We simulated a tiny in-memory one in `level2_librarian.py` using a Python dictionary).

---

**Next Level Info:**

- Now that we can **Generate** (Level 1) and **Retrieve** (Level 2), we will combine them.

- In Level 3, we become **Weavers** and build **RAG** (Retrieval Augmented Generation).
