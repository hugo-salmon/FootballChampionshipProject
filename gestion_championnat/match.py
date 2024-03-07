from rich.console import Console

console = Console()

class Match:
    def __init__(self, score_equipe1, score_equipe2, numero_journee, equipe1, equipe2):
        self.score_equipe1 = score_equipe1
        self.score_equipe2 = score_equipe2
        self.numero_journee = numero_journee
        self.equipe1 = equipe1
        self.equipe2 = equipe2
    
    def afficher(self):
        console.print(f"[bold]Match Journée {self.numero_journee}:[/bold] {self.equipe1.nom} [bold red]{self.score_equipe1}[/bold red] - [bold red]{self.score_equipe2}[/bold red] {self.equipe2.nom}")
