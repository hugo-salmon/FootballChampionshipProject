import datetime
from equipe import Equipe
from championnat import Championnat
from match import Match
from rich.console import Console
import datetime

console = Console()

class GestionChampionnat:
    def __init__(self):
        self.championnats = []


    def ajouter_championnat(self, championnat):
        if any(ch.id == championnat.id for ch in self.championnats):
            print("Erreur: Un championnat avec cet ID existe déjà.")
        else:
            self.championnats.append(championnat)
            

    def trouver_championnat_par_id(self, championnat_id):
        for championnat in self.championnats:
            if championnat.id == championnat_id:
                return championnat
        return None

    def saisir_equipe(self, championnat_id):
        championnat = self.trouver_championnat_par_id(championnat_id)
        if not championnat:
            print(f"Erreur : Aucun championnat trouvé avec l'ID '{championnat_id}'. Veuillez réessayer.")
            return

        id = input("ID de l'Équipe : ")
        for equipe in championnat.equipes:
            if equipe.id == id:
                print("Erreur : Une équipe avec cet ID existe déjà dans ce championnat.")
                return

        nom = input("Nom de l'Équipe : ")
        sigle = input("Sigle du club : ")
        date_creation = input("Année de création : ")
        stade = input("Nom du Stade : ")
        capacite_stade = int(input("Capacité du Stade : "))
        entraineur = input("Nom de l'Entraîneur : ")
        president = input("Nom du Président : ")
        
        nouvelle_equipe = Equipe(id, nom, date_creation, stade, capacite_stade, entraineur, president, sigle)
        if self.ajouter_equipe(championnat_id, nouvelle_equipe):
            print(f"Équipe '{nom}' ajoutée avec succès au championnat '{championnat.nom}'.")
        else:
            print("Erreur lors de l'ajout de l'équipe. Veuillez réessayer.")


    def ajouter_equipe(self, championnat_id, equipe):
        championnat = self.trouver_championnat_par_id(championnat_id)
        if not championnat:
            print("Championnat non trouvé.")
            return False

        if len(championnat.equipes) >= championnat.nombre_equipes:
            print(f"Le championnat '{championnat.nom}' a déjà atteint son nombre maximum d'équipes ({championnat.nombre_equipes}). Impossible d'ajouter '{equipe.nom}'.")
            return False

        if any(e.id == equipe.id for e in championnat.equipes):
            print(f"Erreur : Une équipe avec l'ID {equipe.id} existe déjà dans le championnat '{championnat.nom}'.")
            return False

        championnat.equipes.append(equipe)
        return True

    def ajouter_match(self, championnat_id, match):
        for championnat in self.championnats:
            if championnat.id == championnat_id:
                championnat.matchs.append(match)
                return True
        return False

    
    def saisir_championnat(self):
        id = input("ID du Championnat : ")
        nom = input("Nom du Championnat : ")
        pays = input("Pays : ")
        nombre_equipes = int(input("Nombre d'équipes : "))
        
        while True:
            date_debut_str = input("Date de début (JJ/MM/AAAA) : ")
            date_fin_str = input("Date de fin (JJ/MM/AAAA) : ")
            
            format_date = "%d/%m/%Y"
            try:
                date_debut = datetime.datetime.strptime(date_debut_str, format_date)
                date_fin = datetime.datetime.strptime(date_fin_str, format_date)
            except ValueError:
                print("Erreur de format de date. Veuillez utiliser le format JJ/MM/AAAA.")
                continue
            
            if date_fin <= date_debut:
                print("Erreur : La date de fin doit être postérieure à la date de début. Veuillez saisir à nouveau les dates.")
                continue
            else:
                break
        
        points_gagne = int(input("Points pour un match gagné : "))
        points_perdu = int(input("Points pour un match perdu : "))
        points_nul = int(input("Points pour un match nul : "))

    
        nouveau_championnat = Championnat(id, nom, pays, nombre_equipes, date_debut_str, date_fin_str, points_gagne, points_perdu, points_nul)
        self.ajouter_championnat(nouveau_championnat)
        print(f"Championnat '{nom}' ajouté avec succès.")

    def saisir_resultat_match(self, championnat_id):
        print("Saisie d'un résultat de match.")
        numero_journee = int(input("Numéro de la journée : "))
        id_equipe1 = input("ID de l'équipe 1 : ")
        id_equipe2 = input("ID de l'équipe 2 : ")
        score_equipe1 = int(input("Score de l'équipe 1 : "))
        score_equipe2 = int(input("Score de l'équipe 2 : "))
        
        championnat = None
        for ch in self.championnats:
            if ch.id == championnat_id:
                championnat = ch
                break

        if not championnat:
            print("Championnat non trouvé.")
            return

        equipe1 = equipe2 = None
        for equipe in championnat.equipes:
            if equipe.id == id_equipe1:
                equipe1 = equipe
            elif equipe.id == id_equipe2:
                equipe2 = equipe

        if not equipe1 or not equipe2:
            print("Une ou les deux équipes sont introuvables.")
            return

        nouveau_match = Match(score_equipe1, score_equipe2, numero_journee, equipe1, equipe2)
        championnat.matchs.append(nouveau_match)
        print(f"Match entre {equipe1.nom} et {equipe2.nom} ajouté avec succès.")

    def afficher_championnats(self):
        if not self.championnats:
            console.print("[bold red]Aucun championnat enregistré.[/bold red]", style="bold red")
            return

        print("Liste des championnats :")
        for championnat in self.championnats:
            championnat.afficher()
        
    def afficher_equipes(self, championnat_id):
        championnat_trouve = None
        for championnat in self.championnats:
            if championnat.id == championnat_id:
                championnat_trouve = championnat
                break

        if championnat_trouve:
            print(f"Liste des équipes pour le championnat : {championnat_trouve.nom}")
            if championnat_trouve.equipes:
                for equipe in championnat_trouve.equipes:
                    equipe.afficher()
            else:
                print("Aucune équipe enregistrée pour ce championnat.")
        else:
            print("Championnat non trouvé.")

    def afficher_classement(self, championnat_id):
        championnat = self.trouver_championnat_par_id(championnat_id)
        if championnat:
            championnat.calculer_et_afficher_classement()
        else:
            print(f"Championnat avec l'ID {championnat_id} non trouvé.")