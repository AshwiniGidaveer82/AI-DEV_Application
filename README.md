# AI Dev Agent

This project is an AI-powered development assistant.

## Features

- Uses LLM
- Extensible tools
- Prompt-based responses

## Setup

pip install -r requirements.txt

## Run

python agent.py
=======

# AI-DEV-Agent

# 🚀 AI Dev Agent — Local AI-Powered Developer Assistant (Ollama)

---

# 🧠 Project Overview

AI Dev Agent is a command-line based intelligent assistant designed to simulate a **Senior DevOps Engineer**, powered entirely by **local Large Language Models using Ollama**.

It can:

- Answer technical questions  
- Debug errors  
- Analyze code/files  
- Guide DevOps workflows  

👉 This project demonstrates how to build a **real AI Agent using local LLMs**, without relying on external APIs.

---

# 🎯 Objective of the Project

The goal of this project is to:

- Build a real AI agent using local LLMs  
- Understand AI agent architecture  
- Integrate tools with LLMs  
- Create a cost-free, offline AI system  
- Develop a strong AI + DevOps portfolio project  

---

# 🏗️ Architecture & Flow of Execution

## 🔁 High-Level Flow

User Input → Command Processing → Tool / LLM → Response Generation → Output

---

## 🔍 Detailed Execution Flow

1. **User Input**
   - User enters command in terminal
   - Example: `ask`, `explain error`, `read file`

2. **Command Detection**
   - The agent identifies the command

3. **Decision Layer**
   - If tool-based command → execute tool  
   - Else → send input to LLM  

4. **Tool Execution (if applicable)**
   - File Reader → Reads file content  
   - Error Explainer → Formats debugging prompt  

5. **Prompt Construction**
   - Combines:
     - System prompt (developer personality)
     - User input
     - Tool output

6. **LLM Processing (Ollama)**
   - Local model (e.g., llama3) processes request

7. **Response Output**
   - Printed in terminal using formatted output

---

# ⚙️ Internal Working

The system is built using:

- Python (Core logic)
- LangChain (LLM abstraction)
- Ollama (Local LLM runtime)
- Custom Tools (Actions)
- Prompt Engineering (Behavior control)

---

## 🧩 Core Components

### 1. LLM (Local Brain)

Handled by Ollama using models like:

- llama3
- mistral
- phi3

### 2. Tools Layer

- Error Explainer Tool
- File Reader Tool

### 3. Prompt System

Defines how the agent behaves like a senior developer

### 4. CLI Interface

Handles user interaction via terminal

---

# 🛠️ Features

## ✅ 1. Fully Local AI (No API Required)

- Runs offline
- No cost usage
- Privacy-friendly

## ✅ 2. CLI-Based Chatbot

- Ask any technical question

## ✅ 3. Developer Assistant Mode

- Acts like senior developer
- Gives step-by-step solutions

## ✅ 4. Error Explainer Tool

- Explains errors
- Provides fixes + commands

## ✅ 5. File Reader Tool

- Reads and explains local files

## ✅ 6. Command-Based Interface

- Structured interaction
- Easy to extend

---

# 📂 Project Structure

```
ai-dev-agent/
├── agent.py                 # Main CLI logic & LLM integration
├── requirements.txt         # Python dependencies
├── TODO.md                  # Development tasks
├── README.md                # This documentation
├── prompts/
│   ├── system_prompt.txt    # DevOps engineer personality
│   └── base_prompt.txt      # Base templates
└── tools/
    ├── __init__.py
    ├── error_explainer.py   # Error debugging tool
    ├── file_reader.py       # File content analysis
    └── file_tool.py         # File operations
```

---

# ⚙️ Installation & Setup

## 1. Install Ollama

**Windows:** Download from [ollama.com](https://ollama.com/download)

**Run:** `ollama serve` (start server)

## 2. Pull Model

```bash
ollama pull llama3
```

## 3. Clone/Setup Project

```bash
cd c:/Users/agidavee/ai-dev-agent
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the Agent

```bash
python agent.py
```

**Note:** If langchain_openai error, run `pip install langchain-openai langchain-core>=0.3.0`

# 🧪 Commands

| Command          | Description |
|-----------------|------------|
| ask             | Ask questions |
| explain error   | Debug errors |
| read file       | Analyze files |
| help            | Show commands |
| exit            | Exit program |

---

# 💬 Example Usage

## 🔹 Ask Question

```
$ python agent.py
You: ask
Ask: How to setup Docker on Windows?
Agent: Step-by-step Docker setup...
```

## 🔹 Debug Error

```
You: explain error
Paste error: ModuleNotFoundError: No module named 'langchain_openai'
Agent: Fix: pip install langchain-openai...
```

## 🔹 File Analysis

```
You: read file
Enter file path: agent.py
Agent: This is the main CLI file that...
```

**Pro Tip:** Type `help` for all commands.

# 🧠 Troubleshooting

| Issue | Solution |
|-------|----------|
| Ollama not found | Install from ollama.com & `ollama pull llama3` |
| langchain_openai error | `pip install langchain-openai langchain-core>=0.3.0` |
| SSL/Certifi issues (Windows) | Auto-fixed in agent.py |
| No rich colors | Install `pip install rich` |

# 🔮 Future Enhancements

- Conversation memory
- Autonomous file edits
- Git integration
- Docker deployment
- Web UI (Streamlit)
- Multi-LLM support

---

# 🎯 Conclusion

**Complete documentation created!** AI Dev Agent is now fully documented and ready for use/production/portfolio.

---

By combining:

- Ollama (local AI)
- Tools
- Prompt engineering
- CLI interaction  

👉 It becomes a powerful, cost-free AI system.

---

# ⭐ Final Note

This is not just a chatbot.

👉 It is the **foundation for building autonomous AI systems using local models**
