import json
from pathlib import Path
import typer

app = typer.Typer(help="A simple to-do manager.")
FILE = Path("todos.json")

def load():
    return json.loads(FILE.read_text()) if FILE.exists() else[]

def save(todos):
    FILE.write_text(json.dumps(todos, indent=2))

@app.command()
def add(text: str):
    """Add a task."""
    todos = load()
    todos.append({"text": text, "done": False})
    save(todos)
    typer.echo(f"Added task: {text}")

@app.command("list")
def list_tasks():
    """List all the tasks."""
    for i, t in enumerate(load(), start=1):
        status = "✓" if t["done"] else "✗"
        typer.echo(f"{i}. [{status}] {t['text']}")

@app.command()
def done(index: int):
    """Mark a task as done."""
    todos = load()
    if 0 < index <= len(todos):
        typer.echo("No such task.")
        raise typer.Exit(code=1)
    todos[index - 1]['done']= True
    save(todos)
    typer.echo("Done!")

if __name__ == "__main__":
    app()
  

        
