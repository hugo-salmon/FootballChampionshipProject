from rich.console import Console

console = Console()

class Equipe:
    def __init__(self, id, nom, date_creation, stade, capacite_stade, entraineur, president, sigle):
        self.id = id
        self.nom = nom
        self.date_creation = date_creation
        self.stade = stade
        self.capacite_stade = capacite_stade  
        self.entraineur = entraineur
        self.president = president
        self.sigle = sigle

    def afficher(self):
        console.print(f"[bold magenta]Équipe:[/bold magenta] {self.nom}, [bold red]Sigle:[/bold red] {self.sigle}, [bold yellow]Stade:[/bold yellow] {self.stade} (Capacité: {self.capacite_stade}), [bold cyan]Entraîneur:[/bold cyan] {self.entraineur}, [bold green]Président:[/bold green] {self.president}")