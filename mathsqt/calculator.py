from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from .operations.algebra import AlgebraOperations
from .operations.calculus import CalculusOperations
from .operations.matrix import MatrixOperations
from .operations.binomial import BinomialOperations
from .operations.statistics import StatisticsOperations

console = Console()

class MathCalculator:
    def __init__(self):
        self.algebra = AlgebraOperations()
        self.calculus = CalculusOperations()
        self.matrix = MatrixOperations()
        self.binomial = BinomialOperations()
        self.statistics = StatisticsOperations()
    
    def algebra_operations(self):
        while True:
            console.print(Panel.fit("[bold cyan]Algebra Operations[/bold cyan]"))
            console.print("1. Solve linear equation")
            console.print("2. Solve quadratic equation")
            console.print("3. Simplify expression")
            console.print("b. Back to main menu")
            
            choice = console.input("\n[bold yellow]Select an option: [/bold yellow]").strip().lower()
            
            if choice == 'b':
                break
                
            if choice == '1':
                equation = console.input("Enter linear equation (e.g., 2x + 3 = 7): ")
                self.algebra.solve_linear(equation)
            elif choice == '2':
                equation = console.input("Enter quadratic equation (e.g., x^2 - 5x + 6 = 0): ")
                self.algebra.solve_quadratic(equation)
            elif choice == '3':
                expression = console.input("Enter expression to simplify: ")
                self.algebra.simplify(expression)
            else:
                console.print("[bold red]Invalid choice.[/bold red]")
    
    def calculus_operations(self):
        while True:
            console.print(Panel.fit("[bold cyan]Calculus Operations[/bold cyan]"))
            console.print("1. Differentiate")
            console.print("2. Integrate")
            console.print("3. Find limit")
            console.print("b. Back to main menu")
            
            choice = console.input("\n[bold yellow]Select an option: [/bold yellow]").strip().lower()
            
            if choice == 'b':
                break
                
            if choice == '1':
                expr = console.input("Enter expression to differentiate: ")
                var = console.input("Enter variable: ")
                self.calculus.differentiate(expr, var)
            elif choice == '2':
                expr = console.input("Enter expression to integrate: ")
                var = console.input("Enter variable: ")
                self.calculus.integrate(expr, var)
            elif choice == '3':
                expr = console.input("Enter expression for limit: ")
                var = console.input("Enter variable: ")
                point = console.input("Enter point to approach: ")
                self.calculus.limit(expr, var, point)
            else:
                console.print("[bold red]Invalid choice.[/bold red]")
    
    def matrix_operations(self):
        while True:
            console.print(Panel.fit("[bold cyan]Matrix Operations[/bold cyan]"))
            console.print("1. Add matrices")
            console.print("2. Multiply matrices")
            console.print("3. Find determinant")
            console.print("4. Find inverse")
            console.print("b. Back to main menu")
            
            choice = console.input("\n[bold yellow]Select an option: [/bold yellow]").strip().lower()
            
            if choice == 'b':
                break
                
            if choice == '1':
                self.matrix.add_matrices()
            elif choice == '2':
                self.matrix.multiply_matrices()
            elif choice == '3':
                self.matrix.find_determinant()
            elif choice == '4':
                self.matrix.find_inverse()
            else:
                console.print("[bold red]Invalid choice.[/bold red]")
    
    def binomial_operations(self):
        while True:
            console.print(Panel.fit("[bold cyan]Binomial Operations[/bold cyan]"))
            console.print("1. Expand binomial")
            console.print("2. Calculate binomial coefficient")
            console.print("b. Back to main menu")
            
            choice = console.input("\n[bold yellow]Select an option: [/bold yellow]").strip().lower()
            
            if choice == 'b':
                break
                
            if choice == '1':
                expr = console.input("Enter binomial expression (e.g., (x + y)^3): ")
                self.binomial.expand(expr)
            elif choice == '2':
                n = int(console.input("Enter n: "))
                k = int(console.input("Enter k: "))
                self.binomial.coefficient(n, k)
            else:
                console.print("[bold red]Invalid choice.[/bold red]")
    
    def statistics_operations(self):
        while True:
            console.print(Panel.fit("[bold cyan]Statistics Operations[/bold cyan]"))
            console.print("1. Calculate mean")
            console.print("2. Calculate median")
            console.print("3. Calculate standard deviation")
            console.print("b. Back to main menu")
            
            choice = console.input("\n[bold yellow]Select an option: [/bold yellow]").strip().lower()
            
            if choice == 'b':
                break
                
            if choice == '1':
                data = console.input("Enter data points (comma separated): ")
                self.statistics.calculate_mean(data)
            elif choice == '2':
                data = console.input("Enter data points (comma separated): ")
                self.statistics.calculate_median(data)
            elif choice == '3':
                data = console.input("Enter data points (comma separated): ")
                self.statistics.calculate_std_dev(data)
            else:
                console.print("[bold red]Invalid choice.[/bold red]")
