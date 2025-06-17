import numpy as np
from rich.console import Console
from rich.table import Table

console = Console()

class MatrixOperations:
    def get_matrix(self, prompt):
        console.print(f"\n[bold]{prompt}[/bold]")
        rows = int(console.input("Number of rows: "))
        cols = int(console.input("Number of columns: "))
        
        matrix = []
        for i in range(rows):
            while True:
                try:
                    row_input = console.input(f"Enter row {i+1} (comma-separated values): ")
                    row = [float(x.strip()) for x in row_input.split(',')]
                    if len(row) != cols:
                        console.print(f"[bold red]Error: Expected {cols} values, got {len(row)}[/bold red]")
                        continue
                    matrix.append(row)
                    break
                except ValueError:
                    console.print("[bold red]Error: Please enter numbers separated by commas[/bold red]")
        
        return np.array(matrix)
    
    def display_matrix(self, matrix, title="Result"):
        table = Table(title=title)
        
        for i in range(matrix.shape[1]):
            table.add_column(str(i+1))
        
        for row in matrix:
            table.add_row(*[str(round(x, 4)) for x in row])
        
        console.print(table)
    
    def add_matrices(self):
        try:
            matrix1 = self.get_matrix("Matrix 1")
            matrix2 = self.get_matrix("Matrix 2")
            
            if matrix1.shape != matrix2.shape:
                console.print("[bold red]Matrices must have the same dimensions for addition.[/bold red]")
                return
            
            result = matrix1 + matrix2
            self.display_matrix(result, "Matrix Sum")
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
    
    def multiply_matrices(self):
        try:
            matrix1 = self.get_matrix("Matrix 1")
            matrix2 = self.get_matrix("Matrix 2")
            
            if matrix1.shape[1] != matrix2.shape[0]:
                console.print("[bold red]Number of columns in Matrix 1 must equal number of rows in Matrix 2.[/bold red]")
                return
            
            result = np.matmul(matrix1, matrix2)
            self.display_matrix(result, "Matrix Product")
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
    
    def find_determinant(self):
        try:
            matrix = self.get_matrix("Matrix")
            
            if matrix.shape[0] != matrix.shape[1]:
                console.print("[bold red]Matrix must be square to find determinant.[/bold red]")
                return
            
            det = np.linalg.det(matrix)
            console.print(f"\n[bold green]Determinant:[/bold green] {det:.4f}")
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
    
    def find_inverse(self):
        try:
            matrix = self.get_matrix("Matrix")
            
            if matrix.shape[0] != matrix.shape[1]:
                console.print("[bold red]Matrix must be square to find inverse.[/bold red]")
                return
            
            try:
                inverse = np.linalg.inv(matrix)
                self.display_matrix(inverse, "Matrix Inverse")
            except np.linalg.LinAlgError:
                console.print("[bold red]Matrix is singular and does not have an inverse.[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error: {str(e)}[/bold red]")
