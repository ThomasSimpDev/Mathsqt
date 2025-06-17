from rich.console import Console

console = Console()

def display_error(message):
    console.print(f"[bold red]Error: {message}[/bold red]")

def display_success(message):
    console.print(f"[bold green]{message}[/bold green]")

def display_warning(message):
    console.print(f"[bold yellow]{message}[/bold yellow]")
