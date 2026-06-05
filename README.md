# 🤖 LangGraph ReAct Agent Executor

A lightweight **ReAct (Reasoning + Acting)** agent built using [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain). The agent reasons through problems step-by-step and uses tools to gather real-world information or perform computations.

---

## 🧠 How It Works

The agent follows a **ReAct loop**:

1. **Reason** – The LLM processes the user's message and decides whether to use a tool.
2. **Act** – If a tool is needed, it executes it.
3. **Repeat** – The result is fed back to the LLM until no more tool calls are needed.
4. **Respond** – The final answer is returned to the user.

The flow is visualized and exported as `flow.png` using Mermaid.

---

## 🗂️ Project Structure

```
langgraph-react-agent-executor/
│
├── main.py        # Entry point; defines and compiles the LangGraph state graph
├── nodes.py       # LangGraph node definitions (reasoning + tool execution)
├── react.py       # LLM setup, tool definitions, and tool binding
├── flow.png       # Auto-generated graph visualization (Mermaid)
├── .env           # Environment variables (not committed)
└── README.md
```

---

## 🛠️ Tools Available

| Tool | Description |
|------|-------------|
| `TavilySearch` | Searches the web for real-time information |
| `triple` | Takes a number and returns its triple |

---

> Built with ❤️ using LangGraph and LangChain.
