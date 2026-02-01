import ollama
import sys

# --- LEVEL 5: THE AUTOMATON (AGENT) ---
# Goal: Give the LLM "Hands" (Tools) to interact with the world.
# We will use Ollama's "Tool Calling" feature.

# --- CONFIGURATION ---
HOST = 'http://172.22.112.1:11434'
MODEL = "mistral" # Ensure your model supports tool calling (mistral/llama3 do)

try:
    client = ollama.Client(host=HOST)
except Exception as e:
    sys.exit(1)

# --- THE TOOLS ---
# These are actual Python functions we want the AI to be able to run.

def calculator_tool(expression: str) -> str:
    """
    Evaluates a mathematical expression.
    Arguments:
      expression: The math string to evaluate (e.g., '2 + 2', '15 * 24').
    """
    print(f"🧮 AGENT: Performing calculation: {expression}")
    try:
        # Safety warning: eval is dangerous in prod, but fine for learning here
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

def search_database_tool(query: str) -> str:
    """
    Searches the internal Guild Database for secret information.
    Arguments:
      query: The specific term to look up.
    """
    print(f"🕵️ AGENT: Searching database for: {query}")
    # Simulating the Vector Store lookup from Level 2/3
    db = {
        "password": "The secret password is 'BlueLotus'.",
        "food": "The Guild Master loves Spicy Ramen.",
        "dragon": "The dragon sleeps in the Cavern of Echoes."
    }
    for key in db:
        if key in query.lower():
            return db[key]
    return "No records found in the Guild Archives."

# Define the tool schema for Ollama
my_tools = [
    {
      'type': 'function',
      'function': {
        'name': 'calculator_tool',
        'description': 'Calculate math expressions',
        'parameters': {
          'type': 'object',
          'properties': {
            'expression': {
              'type': 'string',
              'description': 'The math expression to evaluate',
            },
          },
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
          'properties': {
            'query': {
              'type': 'string',
              'description': 'The term to search for (e.g., password, dragon)',
            },
          },
          'required': ['query'],
        },
      },
    },
]

# Map names to actual functions for execution
available_functions = {
    'calculator_tool': calculator_tool,
    'search_database_tool': search_database_tool
}

# --- THE AGENT LOOP ---
def run_agent(user_input):
    print(f"\n👤 User: {user_input}")
    
    # 1. Ask the LLM (with tools enabled)
    response = client.chat(
        model=MODEL,
        messages=[{'role': 'user', 'content': user_input}],
        tools=my_tools
    )
    
    # Check if the model decided to use a tool
    if response.message.tool_calls:
        # 2. ACT (Run the tool)
        for tool in response.message.tool_calls:
            function_name = tool.function.name
            args = tool.function.arguments
            
            print(f"🤖 AGENT DECISION: Call {function_name} with {args}")
            
            func = available_functions.get(function_name)
            if func:
                tool_output = func(**args)
                print(f"✅ TOOL OUTPUT: {tool_output}")
                
                # 3. OBSERVE & RESPOND
                # In a full loop, we'd feed this back to the LLM. 
                # For this simple demo, we just print the result.
                print(f"💬 Final Answer: {tool_output}")
    else:
        # No tool needed, just chat
        print(f"💬 Final Answer: {response.message.content}")

# --- THE QUEST ---
questions = [
    "What is 25 * 45?",               # Needs Calculator
    "Where is the dragon hiding?",    # Needs Search
    "Tell me a joke."                 # Needs mostly Chat
]

print("--- AWAKENING THE AUTOMATON ---")
for q in questions:
    run_agent(q)
    print("-" * 40)
