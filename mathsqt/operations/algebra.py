from sympy import symbols, Eq, solve, simplify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication
from rich.console import Console
import re

console = Console()

# Define transformations for better parsing
transformations = standard_transformations + (implicit_multiplication,)

class AlgebraOperations:
    def _clean_equation(self, equation_str):
        """Clean and prepare the equation string for parsing"""
        # Remove all whitespace
        equation_str = re.sub(r'\s+', '', equation_str)
        # Replace ^ with ** for exponentiation
        equation_str = equation_str.replace('^', '**')
        # Ensure there's a 0 if right side is empty (e.g., "x^2-5x+6=")
        if equation_str.endswith('='):
            equation_str += '0'
        return equation_str

    def solve_linear(self, equation_str):
        try:
            x = symbols('x')
            equation_str = self._clean_equation(equation_str)
            
            if '=' not in equation_str:
                raise ValueError("Equation must contain an equals sign (=)")
                
            parts = equation_str.split('=')
            if len(parts) != 2:
                raise ValueError("Equation must contain exactly one equals sign")
                
            lhs = parse_expr(parts[0], transformations=transformations)
            rhs = parse_expr(parts[1], transformations=transformations)
            equation = Eq(lhs, rhs)
            solution = solve(equation, x)
            
            console.print(f"\n[bold green]Solution:[/bold green]")
            for sol in solution:
                console.print(f"x = {sol.evalf(4)}")  # Display with 4 decimal places
                
        except Exception as e:
            console.print(f"\n[bold red]Error solving equation: {str(e)}[/bold red]")
            console.print("[bold]Please ensure your equation is in the form:[/bold]")
            console.print("[italic]ax + b = c[/italic] (e.g., 2x + 3 = 7)")
    
    def solve_quadratic(self, equation_str):
        try:
            x = symbols('x')
            equation_str = self._clean_equation(equation_str)
            
            if '=' not in equation_str:
                raise ValueError("Equation must contain an equals sign (=)")
                
            parts = equation_str.split('=')
            if len(parts) != 2:
                raise ValueError("Equation must contain exactly one equals sign")
                
            lhs = parse_expr(parts[0], transformations=transformations)
            rhs = parse_expr(parts[1], transformations=transformations)
            equation = Eq(lhs, rhs)
            
            # Solve the equation
            solutions = solve(equation, x)
            
            if not solutions:
                console.print("\n[bold yellow]No real solutions found.[/bold yellow]")
                return
                
            console.print(f"\n[bold green]Solutions:[/bold green]")
            for i, sol in enumerate(solutions, 1):
                if sol.is_real:
                    console.print(f"x{i} = {sol.evalf(4)}")  # Display with 4 decimal places
                else:
                    # Format complex numbers nicely
                    re = sol.as_real_imag()[0].evalf(4)
                    im = sol.as_real_imag()[1].evalf(4)
                    console.print(f"x{i} = {re} {'+' if im >= 0 else '-'} {abs(im)}i")
                    
        except Exception as e:
            console.print(f"\n[bold red]Error solving equation: {str(e)}[/bold red]")
            console.print("[bold]Please ensure your equation is in the form:[/bold]")
            console.print("[italic]ax^2 + bx + c = 0[/italic] (e.g., x^2 - 5x + 6 = 0)")
            console.print("You can use either ^ or ** for exponents")

    def simplify(self, expression_str):
        try:
            expression_str = self._clean_equation(expression_str)
            expr = parse_expr(expression_str, transformations=transformations)
            simplified = simplify(expr)
            
            console.print(f"\n[bold green]Simplified expression:[/bold green]")
            console.print(simplified)
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
            console.print("[bold]Please ensure your expression is valid[/bold]")
