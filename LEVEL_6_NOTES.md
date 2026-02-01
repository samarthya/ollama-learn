# 📜 Level 6 Grimoire: The Mirror (UI)

We have built the brain, but now we must give it a face.

## 🪞 Concept 1: The Session State (`st.session_state`)

Streamlit runs the *entire script* from top to bottom every time you click a button.

- **The Problem**: If `messages = []` was at the top, it would reset to empty every time you hit "Send".
- **The Solution**: `st.session_state` is a dictionary that survives re-runs.
```python
if "messages" not in st.session_state:
    st.session_state.messages = [] # Initialize only once
```

## 👁️ Concept 2: Visualizing Thought (`st.status`)

AI is often a "Black Box". Users trust it more if they see it working.

- **`st.status`**: A container that starts "Running" (spinner) and handles updates.
- We use it to wrap the "Tool Calling" logic.

```python
with st.status("🧠 Thinking...", expanded=True) as status:
    # ... perform slow AI operations ...
    status.update(label="✅ Tools Executed!", state="complete")
```

## 🛠️ Concept 3: The Tool Schema

We don't send *Python functions* to the LLM. We send *Definitions*.

- The **Schema** (JSON) tells the LLM: "I have a tool named X, it takes argument Y."
- The **Mapping** (`available_functions`) tells Python: "If LLM asks for X, run this function code."

**The Flow:**

1.  **Schema**: `{"name": "calc", "param": "expression"}` -> sent to Mistral.
2.  **Mistral**: "I need to calculate. Call `calc` with `2+2`."
3.  **App**: Parses response -> Looks up `calc` in `available_functions` -> Runs `eval("2+2")`.
4.  **App**: Sends `4` back to Mistral.

---

**THE END?**

You have now built a Full Stack AI Application:

- **Backend**: Python + Ollama.
- **Logic**: RAG + Agents.
- **Frontend**: Streamlit.

The only thing left is to **Share it (Containerize)**.
