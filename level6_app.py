import streamlit as st
import ollama
import time
import sys

import os

# --- CONFIGURATION (Win Host Check) ---
# If running in Docker, we grab the env var. If running locally, we fallback to the known IP or localhost.
HOST = os.getenv('OLLAMA_HOST_IP', 'http://172.22.112.1:11434')
MODEL = "mistral"

# --- PAGE SETUP ---
st.set_page_config(page_title="RAG Architect's Mirror", page_icon="🧙‍♂️")
st.title("🧙‍♂️ The RAG Architect's Mirror")
st.caption("Level 6: Visualization of AI Thought")

# --- SESSION STATE INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- CLIENT SETUP ---
@st.cache_resource
def get_client():
    try:
        return ollama.Client(host=HOST)
    except Exception as e:
        st.error(f"Could not connect to Ollama at {HOST}: {e}")
        return None

client = get_client()

# --- BACKEND LOGIC (From Level 5) ---
# We redefine tools here to integrating them into the UI flow

def calculator_tool(expression: str) -> str:
    return str(eval(expression))

def search_database_tool(query: str) -> str:
    # Simulating the Vector Store
    db = {
        "password": "The secret password is 'BlueLotus'.",
        "food": "The Guild Master loves Spicy Ramen.",
        "dragon": "The dragon sleeps in the Cavern of Echoes.",
        "door": "To open the magic door, you must knock three times and whistle."
    }
    results = []
    for key, value in db.items():
        if key in query.lower():
            results.append(value)
    
    if results:
        return "\n".join(results)
    return "No records found in the Guild Archives."

available_functions = {
    'calculator_tool': calculator_tool,
    'search_database_tool': search_database_tool
}

my_tools = [
    {
      'type': 'function',
      'function': {
        'name': 'calculator_tool',
        'description': 'Calculate math expressions',
        'parameters': {
          'type': 'object',
          'properties': {'expression': {'type': 'string'}},
          'required': ['expression'],
        },
      },
    },
    {
      'type': 'function',
      'function': {
        'name': 'search_database_tool',
        'description': 'Search for secret Guild information',
        'parameters': {
          'type': 'object',
          'properties': {'query': {'type': 'string'}},
          'required': ['query'],
        },
      },
    },
]

# --- CHAT UI ---

# 1. Display existing history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 2. Handle User Input
if prompt := st.chat_input("Ask the Automaton (e.g., 'Where is the dragon?')"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Generate Response
    with st.chat_message("assistant"):
        # Placeholder for streaming or thinking
        response_container = st.empty()
        
        # We use a status container to show "Thought Process"
        with st.status("🧠 The Automaton is thinking...", expanded=True) as status:
            
            # Call Ollama
            response = client.chat(
                model=MODEL,
                messages=st.session_state.messages,
                tools=my_tools
            )
            
            # Check for Tools
            if response.message.tool_calls:
                
                for tool in response.message.tool_calls:
                    func_name = tool.function.name
                    args = tool.function.arguments
                    
                    st.write(f"🛠️ **Decided to call:** `{func_name}`")
                    st.json(args)
                    
                    # Execute
                    func = available_functions.get(func_name)
                    if func:
                        output = func(**args)
                        st.write(f"✅ **Tool Output:** `{output}`")
                        
                        # Append tool result to history so the model knows it
                        # Note: In a real app we'd append a tool message, but for this demo 
                        # we'll just force the final answer generation with the context.
                        
                        final_prompt = f"The user asked: {prompt}. The tool {func_name} returned: {output}. Answer the user."
                        
                        final_res = client.generate(model=MODEL, prompt=final_prompt, stream=False)
                        final_answer = final_res['response']
                        
                        status.update(label="✅ Tools Executed!", state="complete", expanded=False)
                        response_container.markdown(final_answer)
                        
                        # Save assistant response
                        st.session_state.messages.append({"role": "assistant", "content": final_answer})
            else:
                # Direct Answer
                final_answer = response.message.content
                status.update(label="✅ Meaning Generated", state="complete", expanded=False)
                response_container.markdown(final_answer)
                st.session_state.messages.append({"role": "assistant", "content": final_answer})
