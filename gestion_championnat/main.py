from gestion_championnat import GestionChampionnat

def afficher_menu():
    print("\nGestionnaire de championnats")
    print("1. Ajouter un championnat")
    print("2. Ajouter une équipe à un championnat")
    print("3. Saisir le résultat d'un match")
    print("4. Afficher les championnats")
    print("5. Afficher la liste des équipes d'un championnat")
    print("6. Afficher le classement d'un championnat")
    print("7. Quitter l'application")

def main():
    gestionnaire = GestionChampionnat()
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            gestionnaire.saisir_championnat()
        elif choix == "2":
            championnat_id = input("Entrez l'ID du championnat : ")
            gestionnaire.saisir_equipe(championnat_id)
        elif choix == "3":
            championnat_id = input("Entrez l'ID du championnat : ")
            gestionnaire.saisir_resultat_match(championnat_id)
        elif choix == "4":
            gestionnaire.afficher_championnats()
        elif choix == "5":
            championnat_id = input("Entrez l'ID du championnat : ")
            gestionnaire.afficher_equipes(championnat_id)
        elif choix == "6":
            championnat_id = input("Entrez l'ID du championnat : ")
            gestionnaire.afficher_classement(championnat_id)
        elif choix == "7":
            print("Merci d'utiliser le gestionnaire de championnats. À bientôt !")
            break
        else:
            print("Choix non reconnu. Veuillez réessayer.")

if __name__ == "__main__":
    main()
