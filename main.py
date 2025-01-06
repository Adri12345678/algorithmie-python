from gestion_produits import GestionProduits
from gestion_utilisateurs import GestionUtilisateurs


def menu_admin():
    gestion_utilisateurs = GestionUtilisateurs()

    while True:
        print("\n--- Menu Gestion des Utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Vérifier si un mot de passe est compromis")
        print("4. Afficher la liste des utilisateurs")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            gestion_utilisateurs.ajouter_utilisateur()

        elif choix == "2":
            gestion_utilisateurs.supprimer_utilisateur()

        elif choix == "3":
            mot_de_passe = input("Entrez le mot de passe à vérifier : ")
            if gestion_utilisateurs.verifier_compromis(mot_de_passe):
                print("⚠️ Le mot de passe est compromis !")
            else:
                print("✅ Le mot de passe est sûr.")

        elif choix == "4":
            gestion_utilisateurs.afficher_utilisateurs()

        elif choix == "5":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


def menu_utilisateurs(utilisateur):
    gestion_produits = GestionProduits(f"produits_{utilisateur}.csv")

    while True:
        print(f"\n--- Menu Gestion des Produits pour {utilisateur} ---")
        print("\n1. Afficher la liste des produits")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Rechercher un produit")
        print("5. Trier la liste des produits")
        print("6. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            gestion_produits.afficher_produits()

        elif choix == "2":
            gestion_produits.ajouter_produit()

        elif choix == "3":
            gestion_produits.supprimer_produit()

        elif choix == "4":
            print("1. recherche normale")
            print("2. recherche binaire")
            algo = input("Choisissez un algorithme de recherche : ")
            if algo == '1':
                gestion_produits.rechercher_produit()
            elif algo == '2':
                gestion_produits.recherche_binaire()
            else:
                print("Algorithme invalide.")

        elif choix == "5":
            print("1. trier par tri rapide")
            print("2. trier par tri à bulle")
            algo = input("Choisissez un algorithme de tri : ")
            if algo == '1':
                gestion_produits.tri_rapide()
            elif algo == '2':
                gestion_produits.tri_bulles()
            else:
                print("Algorithme invalide.")

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, essayez encore.")


def main():
    
    gestion_utilisateurs = GestionUtilisateurs()
    print("\n--- Bienvenue dans le Gestionnaire ---")
    
    while True:
        print("\n1. Se connecter")
        print("2. Créer un compte")
        print("3. Quitter")
        
        choix = input("\nVotre choix : ")
        if choix == "1":
            nom_utilisateur = input("Nom d'utilisateur : ")
            mot_de_passe = input("Mot de passe : ")
            if gestion_utilisateurs.verifier_utilisateur(nom_utilisateur, mot_de_passe):
                print(f"Bienvenue, {nom_utilisateur} !")
                if nom_utilisateur == "admin":
                    menu_admin()
                else:
                    menu_utilisateurs(utilisateur=nom_utilisateur)
                break
            else:
                print("❌ Nom d'utilisateur ou mot de passe incorrect.")
        elif choix == "2":
            gestion_utilisateurs.ajouter_utilisateur()
        elif choix == "3":
            print("Au revoir !")
            exit()
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()

