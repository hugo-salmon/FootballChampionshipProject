from rich.console import Console
from rich.table import Table

console = Console()

class Championnat:
    def __init__(self, id, nom, pays, nombre_equipes, date_debut, date_fin, points_gagne, points_perdu, points_nul):
        self.id = id
        self.nom = nom
        self.pays = pays
        self.nombre_equipes = nombre_equipes
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.points_gagne = points_gagne
        self.points_perdu = points_perdu
        self.points_nul = points_nul
        self.equipes = []
        self.matchs = []

    def afficher(self):
        console.print(f"[bold magenta]Championnat:[/bold magenta] {self.nom}, [bold cyan]Pays:[/bold cyan] {self.pays}, [bold yellow]De {self.date_debut} à {self.date_fin},[/bold yellow] [bold green]Nombre d'équipes:[/bold green] {self.nombre_equipes}")


    def calculer_et_afficher_classement(self):
        classement = []
        for equipe in self.equipes:
            matches_joues = sum(1 for match in self.matchs if equipe in [match.equipe1, match.equipe2])
            matches_gagnes = sum(1 for match in self.matchs if (equipe == match.equipe1 and match.score_equipe1 > match.score_equipe2) or (equipe == match.equipe2 and match.score_equipe2 > match.score_equipe1))
            matches_perdus = sum(1 for match in self.matchs if (equipe == match.equipe1 and match.score_equipe1 < match.score_equipe2) or (equipe == match.equipe2 and match.score_equipe2 < match.score_equipe1))
            matches_nuls = sum(1 for match in self.matchs if match.score_equipe1 == match.score_equipe2 and equipe in [match.equipe1, match.equipe2])
            buts_marques = sum(match.score_equipe1 if equipe == match.equipe1 else match.score_equipe2 for match in self.matchs if equipe in [match.equipe1, match.equipe2])
            buts_concedes = sum(match.score_equipe2 if equipe == match.equipe1 else match.score_equipe1 for match in self.matchs if equipe in [match.equipe1, match.equipe2])
            difference_buts = buts_marques - buts_concedes
            total_points = (matches_gagnes * self.points_gagne) + (matches_nuls * self.points_nul)
            
            classement.append((equipe, total_points, matches_joues, matches_gagnes, matches_perdus, matches_nuls, buts_marques, buts_concedes, difference_buts))

        classement.sort(key=lambda x: (x[1], x[8]), reverse=True)

        table = Table(title=f"Classement du championnat {self.nom}")
        table.add_column("Position", justify="right", style="cyan", no_wrap=True)
        table.add_column("Équipe", style="magenta")
        table.add_column("Points", justify="right", style="green")
        table.add_column("Joués", justify="right", style="yellow")
        table.add_column("Gagnés", justify="right", style="yellow")
        table.add_column("Perdus", justify="right", style="yellow")
        table.add_column("Nuls", justify="right", style="yellow")
        table.add_column("Buts marqués", justify="right", style="green")
        table.add_column("Buts concédés", justify="right", style="green")
        table.add_column("Différence de buts", justify="right", style="blue")
        
        for i, (equipe, points, mj, mg, mp, mn, bm, bc, db) in enumerate(classement, 1):
            db_formatted = f"+{db}" if db > 0 else str(db)
            table.add_row(str(i), equipe.nom, str(points), str(mj), str(mg), str(mp), str(mn), str(bm), str(bc), db_formatted)

        console.print(table)