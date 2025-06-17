import numpy as np
from rich.console import Console

console = Console()

class StatisticsOperations:
    def parse_data(self, data_str):
        try:
            return [float(x.strip()) for x in data_str.split(',')]
        except ValueError:
            console.print("[bold red]Invalid data format. Please enter numbers separated by commas.[/bold red]")
            return None
    
    def calculate_mean(self, data_str):
        data = self.parse_data(data_str)
        if data:
            mean = np.mean(data)
            console.print(f"\n[bold green]Mean:[/bold green] {mean:.4f}")
    
    def calculate_median(self, data_str):
        data = self.parse_data(data_str)
        if data:
            median = np.median(data)
            console.print(f"\n[bold green]Median:[/bold green] {median:.4f}")
    
    def calculate_std_dev(self, data_str):
        data = self.parse_data(data_str)
        if data:
            std_dev = np.std(data)
            console.print(f"\n[bold green]Standard Deviation:[/bold green] {std_dev:.4f}")
