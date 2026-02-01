# 📜 Level 4 Grimoire: The Critic

You have built the Weaver, but it is gullible. It tries to answer even when the books are wrong. Now you become the **Critic**.

## ⚖️ Concept 1: The Critic Loop

We don't just blindly trust the retrieval. We add a validation step.

1.  **Retrieve**: Get context.
2.  **Judge**: Ask the LLM (as a separate agent), "Does this context actually answer the question?"
3.  **Act**: 
    - If **YES**: Proceed to Generate answer.
    - If **NO**: Fallback ("I don't know") or Search Web (Level 5).

## 🚫 Concept 2: Grounding vs Hallucination

- **Hallucination**: The model makes up an answer not in the data.
- **Grounding**: Ensuring the answer is supported by the specific context provided.
- The Critic forces **Grounding** by rejecting irrelevant context.

## 🤖 The Prompt

The Judge's spell is simple:

> "You are a strict judge. Does the Context answer the Question? YES or NO."

By asking for a boolean classification, we turn the squishy language task into a hard logic gate.

---

**Next Level Info:**

What if the Critic says NO? What if we need to calculate `2 + 2`?
In Level 5, we become **Agents** and give the LLM **Tools**.
