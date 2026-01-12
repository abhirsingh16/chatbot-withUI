# AI Chatbot with Streamlit UI

A production-ready conversational AI chatbot built with LangChain, LangGraph, Groq LLM, and Streamlit. Features advanced capabilities including tool calling, response streaming, and conversation threading for context-aware interactions.

## 🚀 Features

- **Streamlit Frontend**: Clean, responsive web interface for real-time chat interactions
- **Groq LLM Integration**: Lightning-fast inference using Groq's optimized LLM infrastructure
- **LangChain Framework**: Modular architecture for prompt management and LLM orchestration
- **LangGraph Workflows**: State machine-based conversation flows with multi-step reasoning
- **Tool Calling**: Dynamic function execution for extended capabilities (web search, calculations, data retrieval)
- **Response Streaming**: Token-by-token streaming for improved user experience
- **Conversation Threading**: Persistent memory and context management across chat sessions

## 🏗️ Architecture

```
┌─────────────────┐
│  Streamlit UI   │
│   (Frontend)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   LangGraph     │
│  State Machine  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────┐
│   LangChain     │◄────►│  Tool Layer  │
│   Orchestrator  │      │  (Functions) │
└────────┬────────┘      └──────────────┘
         │
         ▼
┌─────────────────┐
│   Groq LLM API  │
└─────────────────┘
```

## 📋 Prerequisites

- Python 3.12+
- Groq API Key ([Get it here](https://console.groq.com))
- pip or conda package manager

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/chatbot-withUI.git
cd chatbot-withUI
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
```


```

## 📦 Dependencies

```txt
streamlit>=1.28.0
langchain>=0.1.0
langgraph>=0.0.20
groq>=0.4.0
python-dotenv>=1.0.0
```

## 🚦 Usage

### Running the Application

```bash
streamlit run app.py
```

The app will start on `http://localhost:8501`

### Basic Interaction

1. Enter your message in the chat input box
2. Watch responses stream in real-time
3. Use available tools by asking relevant questions
4. Context is maintained across the conversation thread

### Example Queries

```python
# Simple conversation
"Hello! How are you?"

# Tool calling
"What's the weather in Mumbai?"
"Search for recent AI news"

# Multi-step reasoning
"Calculate 15% of 250, then multiply by 3"
```

## 🔧 Configuration

### Customizing LLM Parameters

Edit `config.py`:

```python
LLM_CONFIG = {
    "model": "mixtral-8x7b-32768",
    "temperature": 0.7,
    "max_tokens": 1024,
    "streaming": True
}
```

### Adding Custom Tools

Create tools in `tools/custom_tools.py`:

```python
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluates mathematical expressions"""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

## 🧠 Key Concepts

### 1. **Tool Calling**
The chatbot can dynamically invoke external functions based on user queries. Tools are registered with LangChain and automatically selected by the LLM when needed.

```python
tools = [search_tool, calculator_tool, weather_tool]
agent = create_tool_calling_agent(llm, tools)
```

### 2. **Response Streaming**
Tokens are streamed from Groq LLM and displayed incrementally in the UI for better UX.

```python
for chunk in agent.stream({"input": user_message}):
    st.write(chunk)
```

### 3. **Conversation Threading**
LangGraph maintains conversation state across turns using thread IDs:

```python
config = {"configurable": {"thread_id": session_id}}
response = agent.invoke(user_input, config=config)
```


## 🤝 Contributing

Contributions welcome! Please open an issue or submit a PR.

## 📧 Contact

**Abhishek Ramesh Singh**  
📧 abhirsingh16@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/abhirsingh16) | [GitHub](https://github.com/abhirsingh16)

---

⭐ Star this repo if you find it useful!