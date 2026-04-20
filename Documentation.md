# 🚀 AI Dev Agent — Project Documentation

---

# 📌 1. Project Overview

The **AI Dev Agent** is a command-line-based intelligent assistant designed to help developers perform common development and DevOps tasks using AI.

It combines:

* Local LLMs (via Ollama)
* Optional cloud models (OpenAI)
* Custom tools (error debugging, file analysis)

This project demonstrates how to build a **real AI agent system**, not just a chatbot.

---

# 🎯 2. Purpose of the Project

The main goal of this project is to:

* Build a **real-world AI agent**
* Understand **LLM integration**
* Learn **tool-based AI architecture**
* Create a **developer productivity assistant**
* Practice **CLI-based system design**

---

# 🧠 3. What is an AI Agent?

An AI agent is a system that:

1. Takes input from user
2. Understands intent
3. Decides action
4. Uses tools if required
5. Produces intelligent output

---

# ⚙️ 4. System Architecture

```
User (CLI)
   ↓
agent.py (Controller)
   ↓
Command Parser
   ↓
-------------------------
| Tool OR LLM Decision |
-------------------------
   ↓
LLM (Ollama / OpenAI)
   ↓
Response
   ↓
Terminal Output
```

---

# 📂 5. Project Structure

```
ai-dev-agent/
│
├── agent.py                 # Main program (brain controller)
├── tools/
│   ├── error_explainer.py   # Debugging tool
│   └── file_reader.py       # File analysis tool
│
├── prompts/
│   └── system_prompt.txt    # Agent personality
│
├── .env                     # API key storage (optional)
├── README.md                # Project description
└── DOCUMENTATION.md         # This file
```

---

# 🧩 6. Key Components Explanation

---

## 🔹 agent.py (Main Controller)

This is the core of the system.

Responsibilities:

* Takes user input
* Parses commands
* Decides which tool or model to use
* Sends request to LLM
* Displays output

---

## 🔹 Tools (AI Capabilities)

### 1. Error Explainer

* Takes error input
* Explains:

  * Meaning
  * Cause
  * Fix
  * Solution command

---

### 2. File Reader

* Reads local files
* Sends content to AI
* Provides explanation

---

## 🔹 System Prompt

Defines agent personality:

* Senior developer tone
* Step-by-step explanation
* Focus on DevOps topics

---

## 🔹 LLM Integration

Supports:

### 1. Local Model (Default)

* Ollama (llama3, mistral, phi3)
* Free and offline

### 2. Cloud Model (Fallback)

* OpenAI API
* Requires API key

---

# 💻 7. CLI Usage

---

## Available Commands

```
help            → Show commands
ask             → Ask general questions
explain error   → Debug errors
read file       → Analyze file
exit            → Exit program
```

---

## Example Usage

```
You: ask
Ask: What is Docker?

You: explain error
Paste error: ModuleNotFoundError: No module named 'pymongo'

You: read file
Enter file path: Dockerfile
```

---

# 🔄 8. Flow of Execution

```
Start Program
   ↓
Display CLI Menu
   ↓
User Input
   ↓
Command Detection
   ↓
IF Tool → Execute Tool
ELSE → Send to LLM
   ↓
Generate Response
   ↓
Display Output
   ↓
Repeat
```

---

# 🐧 9. Execution Steps (WSL/Linux)

```
cd ai-dev-agent
python3 -m venv venv
source venv/bin/activate
pip install langchain langchain-ollama python-dotenv rich

ollama pull llama3
ollama serve

python agent.py
```

---

# 🪟 10. Execution Steps (Windows)

```
venv\Scripts\activate
pip install langchain langchain-ollama python-dotenv rich

python agent.py
```

---

# ⚠️ 11. Common Issues & Fixes

---

## Issue: Module Not Found

👉 Install dependencies using pip

---

## Issue: SSL Certificate Error

👉 Use certifi in code

---

## Issue: Ollama Model Not Found

```
ollama pull llama3
```

---

## Issue: API Key Error

👉 Add correct key in `.env`

---

# ✨ 12. Features

* CLI-based AI assistant
* Tool-based architecture
* Local LLM support (offline)
* Error debugging automation
* File analysis capability
* Clean modular design

---

# 🚀 13. Future Enhancements

* Web UI (React)
* Chat memory (context awareness)
* DevOps automation (Docker/K8s commands)
* Multi-agent system
* Voice interface

---

# 📚 14. Learnings from This Project

* How LLMs work in real applications
* Prompt engineering techniques
* Tool-based AI design
* CLI application development
* Environment management (venv, WSL)
* Debugging real-world issues

---

# 🏁 15. Conclusion

This project demonstrates how to move from:

❌ Simple chatbot
➡️
✅ Real AI-powered developer assistant

It provides a strong foundation for building:

* AI tools
* DevOps automation agents
* Intelligent developer systems

---

# 🎯 Final Summary

> AI Dev Agent is a CLI-based intelligent assistant that uses LLMs and tools to help developers automate tasks, debug errors, and understand code efficiently.

---
