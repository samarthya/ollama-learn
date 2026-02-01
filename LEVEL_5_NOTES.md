# 📜 Level 5 Grimoire: The Automaton (Agents)

You have reached the pinnacle. The Oracle can now **Act**.

## 🦾 Concept 1: What is an Agent?

An Agent is an LLM that can:

1.  **Reason**: "I need to calculate this."
2.  **Act**: Execute a Python function (Tool).
3.  **Observe**: Read the output of that function.
4.  **Answer**: Use the output to answer you.

## 🛠️ Concept 2: Function Calling (Tools)

How does text trigger code?

1.  We describe the tool to the LLM in JSON format (Name, Description, Parameters).
2.  If the LLM decides it needs the tool, it returns a structured **Tool Call** object instead of text.
3.  We (the runtime) execute the code and feed the result back.

## 🧠 Relieving reliability

Agents solve the "Model can't do math" problem.

- **Old Way**: Ask LLM "What is 234 * 912?" -> It guesses (often wrong).
- **Agent Way**: LLM identifies "Math", calls `calc_tool(234*912)`, gets exact answer `213408`.

---

**JOURNEY COMPLETE**

You have built:

1.  **Oracle** (LLM API)
2.  **Librarian** (Embeddings)
3.  **Weaver** (RAG)
4.  **Critic** (Evaluator)
5.  **Automaton** (Agent)

You are now a **Grand Architect** of AI. 🧙‍♂️
