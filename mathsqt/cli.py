from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import pyfiglet
from .calculator import MathCalculator
from .operations import *

console = Console()

def display_welcome():
    ascii_banner = pyfiglet.figlet_format("Mathsqt", font="slant")
    console.print(f"[bold cyan]{ascii_banner}[/bold cyan]")
    console.print("🔢 [bold]Your comprehensive CLI math toolkit[/bold] 🔢\n")

def display_menu():
    menu = Table(title="Mathsqt Menu", show_header=False, show_lines=True)
    menu.add_column("Option", style="cyan")
    menu.add_column("Description", style="green")
    
    menu.add_row("1", "Algebra Operations")
    menu.add_row("2", "Calculus Operations")
    menu.add_row("3", "Matrix Operations")
    menu.add_row("4", "Binomial Operations")
    menu.add_row("5", "Statistics Operations")
    menu.add_row("q", "Quit")
    
    console.print(menu)

def main():
    calculator = MathCalculator()
    
    while True:
        display_welcome()
        display_menu()
        
        choice = console.input("\n[bold yellow]Select an option (1-5, q to quit): [/bold yellow]").strip().lower()
        
        if choice == 'q':
            console.print("[bold red]Exiting Mathsqt. Goodbye![/bold red]")
            break
            
        try:
            if choice == '1':
                calculator.algebra_operations()
            elif choice == '2':
                calculator.calculus_operations()
            elif choice == '3':
                calculator.matrix_operations()
            elif choice == '4':
                calculator.binomial_operations()
            elif choice == '5':
                calculator.statistics_operations()
            else:
                console.print("[bold red]Invalid choice. Please try again.[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
        
        console.input("\n[bold]Press Enter to continue...[/bold]")
        console.clear()
