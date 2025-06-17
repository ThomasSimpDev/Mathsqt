from sympy import symbols, expand, binomial
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication
from rich.console import Console
import re

console = Console()

# Define transformations for better parsing
transformations = standard_transformations + (implicit_multiplication,)

class BinomialOperations:
    def _clean_expression(self, expr_str):
        """Clean and prepare the expression string for parsing"""
        # Remove all whitespace
        expr_str = re.sub(r'\s+', '', expr_str)
        # Replace ^ with ** for exponentiation
        expr_str = expr_str.replace('^', '**')
        return expr_str

    def expand(self, expr_str):
        try:
            expr_str = self._clean_expression(expr_str)
            expr = parse_expr(expr_str, transformations=transformations)
            expanded = expand(expr)
            
            console.print(f"\n[bold green]Expanded form:[/bold green]")
            console.print(expanded)
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
            console.print("[bold]Please ensure your expression is in the form:[/bold]")
            console.print("[italic](a + b)^n[/italic] (using ^ or ** for exponent)")
            console.print("Example: (x + y)^3 or (2*x - 3)**2")

    def coefficient(self, n, k):
        try:
            coeff = binomial(n, k)
            console.print(f"\n[bold green]Binomial coefficient C({n}, {k}):[/bold green] {coeff}")
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
