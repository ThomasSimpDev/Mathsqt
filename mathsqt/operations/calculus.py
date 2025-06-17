from sympy import symbols, diff, integrate, limit, oo
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication
from rich.console import Console
import re

console = Console()

# Define transformations for better parsing
transformations = standard_transformations + (implicit_multiplication,)

class CalculusOperations:
    def _clean_expression(self, expr_str):
        """Clean and prepare the expression string for parsing"""
        # Remove all whitespace
        expr_str = re.sub(r'\s+', '', expr_str)
        # Replace ^ with ** for exponentiation
        expr_str = expr_str.replace('^', '**')
        return expr_str

    def differentiate(self, expr_str, var_str):
        try:
            var = symbols(var_str)
            expr_str = self._clean_expression(expr_str)
            expr = parse_expr(expr_str, transformations=transformations)
            derivative = diff(expr, var)
            
            console.print(f"\n[bold green]Derivative with respect to {var_str}:[/bold green]")
            console.print(derivative)
        except Exception as e:
            console.print(f"\n[bold red]Error differentiating expression: {str(e)}[/bold red]")
            console.print("[bold]Please ensure your expression is in the form:[/bold]")
            console.print("[italic]ax^n + bx + c[/italic] (using ^ or ** for exponents)")
            console.print("Example: y^2 - 2y + 5 or y**2 - 2*y + 5")

    def integrate(self, expr_str, var_str):
        try:
            var = symbols(var_str)
            expr_str = self._clean_expression(expr_str)
            expr = parse_expr(expr_str, transformations=transformations)
            integral = integrate(expr, var).simplify()
            
            console.print(f"\n[bold green]Integral with respect to {var_str}:[/bold green]")
            console.print(f"{integral} + C")
        except Exception as e:
            console.print(f"\n[bold red]Error integrating expression: {str(e)}[/bold red]")
            console.print("[bold]Please ensure your expression is in the form:[/bold]")
            console.print("[italic]ax^n + bx + c[/italic] (using ^ or ** for exponents)")

    def limit(self, expr_str, var_str, point_str):
        try:
            var = symbols(var_str)
            expr_str = self._clean_expression(expr_str)
            expr = parse_expr(expr_str, transformations=transformations)
            
            if point_str.lower() == 'infinity':
                point = oo
            elif point_str.lower() == '-infinity':
                point = -oo
            else:
                point = parse_expr(point_str, transformations=transformations)
            
            lim = limit(expr, var, point)
            
            console.print(f"\n[bold green]Limit as {var_str} approaches {point_str}:[/bold green]")
            console.print(lim)
        except Exception as e:
            console.print(f"\n[bold red]Error finding limit: {str(e)}[/bold red]")
            console.print("[bold]Please ensure your input is in the correct form:[/bold]")
            console.print("Expression example: (x^2 - 1)/(x - 1)")
            console.print("Point can be a number, 'infinity', or '-infinity'")
