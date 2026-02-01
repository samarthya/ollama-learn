# 📜 Level 1 Grimoire: The Foundation

Welcome to the start of your journey, **Architect**. Before we build complex structures, we must understand the fundamental magic: 

- **The LLM**.

## 🔮 Concept 1: The Oracle (Large Language Model)

The "Oracle" you summoned is not a person. It is a **Next Token Prediction Engine**.

- It does not "know" things; it predicts what word comes next based on patterns it learned from massive amounts of text.
- It is **Stateless**. If you ask it "What is my name?" it won't know, even if you told it 5 seconds ago, unless you send that history back to it.

## 💧 Concept 2: Mana (Tokens)

Computers don't read words; they read numbers.

- **Tokenization**: Turning text into numbers.
- "The sky is blue" -> `[482, 9552, 318, 2645]`
- Approx 1,000 tokens ≈ 750 words.
- **Context Window**: The maximum amount of Mana (tokens) the model can hold in its "mind" at once.

## 🌡️ Concept 3: Temperature (Chaos)

- **Low Temperature (0.0 - 0.3)**: The Oracle is focused, deterministic. Good for coding and facts.
- **High Temperature (0.7-1.0)**: The Oracle is creative, random. Good for stories.

## 🛠️ The Spell (Code Breakdown)

In `level1_oracle.py`:

1.  `client = ollama.Client(...)`: We open a portal to the engine.
2.  `model_name = "mistral"`: We choose which spirit to summon.
3.  `stream=True`: We don't wait for the full answer; we watch the prophecy unfold (token by token).

---

**Next Level Info:**
Now that we can talk to the Oracle, we need to give it **Memory**.
In Level 2, we will become **Librarians** and learn about **Embeddings**.
