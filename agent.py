import os
import certifi
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import httpx
from rich import print
from pathlib import Path

# Tools
from tools.error_explainer import explain_error
from tools.file_reader import read_file

# Fix SSL issue (Windows)
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

# Load environment variables
load_dotenv()

# Try Ollama first (free), fallback to OpenAI
try:
    llm = ChatOllama(model="llama3")
    print("[green]Using Ollama (llama3)[/green]")
except:
    print("[yellow]Ollama not available, using OpenAI[/yellow]")
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        http_client=httpx.Client(verify=False)
    )

# Load system prompt
try:
    system_prompt = Path("prompts/system_prompt.txt").read_text()
except:
    system_prompt = "You are a Senior DevOps Engineer."

# UI
print("[bold green]🚀 AI Dev Agent Started[/bold green]")
print("[yellow]Commands: help | ask | explain error | read file | exit[/yellow]")
print("[blue]Install Ollama from ollama.com & run 'ollama pull llama3' for free unlimited use![/blue]\n")

while True:
    user_input = input("You: ").strip().lower()

    # Exit
    if user_input == "exit":
        print("[red]👋 Exiting...[/red]")
        break

    # Help
    if user_input == "help":
        print("""
[cyan]Commands:[/cyan]
- ask → Ask anything
- explain error → Debug errors
- read file → Analyze files
- help → Show commands
- exit → Quit
        """)
        continue

    # Ask normal question
    if user_input == "ask":
        question = input("Ask: ")
        full_prompt = system_prompt + "\nUser: " + question
        response = llm.invoke(full_prompt)
        print("[green]Agent:[/green]", response.content)
        continue

    # Error Explainer Tool
    if user_input == "explain error":
        error = input("Paste error: ")
        prompt = explain_error(error)
        response = llm.invoke(prompt)
        print("[green]Agent:[/green]", response.content)
        continue

    # File Reader Tool
    if user_input == "read file":
        path = input("Enter file path: ")
        content = read_file(path)

        prompt = f"""
        You are a senior developer.

        Explain this file step by step:

        {content}
        """

        response = llm.invoke(prompt)
        print("[green]Agent:[/green]", response.content)
        continue

    # Default fallback (direct question)
    full_prompt = system_prompt + "\nUser: " + user_input
    response = llm.invoke(full_prompt)
    print("[green]Agent:[/green]", response.content)
