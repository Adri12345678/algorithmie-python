from gestion_produits import GestionProduits
from gestion_utilisateurs import GestionUtilisateurs

def menu_utilisateur():
    gestion_utilisateurs = GestionUtilisateurs()

    while True:
        print("\n--- Menu Gestion des Utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Vérifier si un mot de passe est compromis")
        print("4. Afficher la liste des utilisateurs")
        print("5. Quitter le menu utilisateur")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            nom = input("Entrez le nom de l'utilisateur : ")
            mot_de_passe = input("Entrez le mot de passe : ")
            gestion_utilisateurs.ajouter_utilisateur(nom, mot_de_passe)
        elif choix == "2":
            nom = input("Entrez le nom de l'utilisateur à supprimer : ")
            gestion_utilisateurs.supprimer_utilisateur(nom)
        elif choix == "3":
            mot_de_passe = input("Entrez le mot de passe à vérifier : ")
            if gestion_utilisateurs.verifier_compromis(mot_de_passe):
                print("⚠️ Le mot de passe est compromis !")
            else:
                print("✅ Le mot de passe est sûr.")
        elif choix == "4":
            print("Liste des utilisateurs :")
            for utilisateur in gestion_utilisateurs.utilisateurs:
                print(f"- {utilisateur['nom_utilisateur']}")
        elif choix == "5":
            print("Retour au menu principal...")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_produits():
    gestionnaire = GestionProduits("produits.csv")

    while True:
        print("\n--- Menu Gestion des Produits ---")
        print("1. Afficher la liste des produits")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Rechercher un produit")
        print("5. Trier la liste des produits")
        print("6. Quitter le menu produits")

        choix = input("Choisissez une option : ")

        if choix == "1":
            gestionnaire.afficher_produits()

        elif choix == "2":
            gestionnaire.ajouter_produit()

        elif choix == "3":
            gestionnaire.supprimer_produit()

        elif choix == "4":
            print("1. recherche normale")
            print("2. recherche binaire")
            algo = input("Choisissez un algorithme de recherche : ")
            if algo == '1':
                gestionnaire.rechercher_produit()
            elif algo == '2':
                gestionnaire.recherche_binaire()
            else:
                print("Algorithme invalide.")

        elif choix == "5":
            print("1. trier par tri rapide")
            print("2. trier par tri à bulle")
            algo = input("Choisissez un algorithme de tri : ")
            if algo == '1':
                gestionnaire.tri_rapide()
            elif algo == '2':
                gestionnaire.tri_bulles()
            else:
                print("Algorithme invalide.")

        elif choix == "6":
            print("Retour au menu principal...")
            break

        else:
            print("Choix invalide, essayez encore.")


def afficher_menu():
    print("\n--- Menu Principal ---")
    print("1. Gestion des produits")
    print("2. Gestion des utilisateurs")
    print("3. Quitter")

def main():
    
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            menu_produits()
        elif choix == "2":
            menu_utilisateur()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
