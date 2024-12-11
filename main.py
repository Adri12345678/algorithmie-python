from gestion_produits import *

def afficher_menu():
    print("\n--- Menu Principal ---")
    print("1. Afficher la liste des produits")
    print("2. Ajouter un produit")
    print("3. Supprimer un produit")
    print("4. Rechercher un produit")
    print("5. Trier la liste des produits")
    print("6. Quitter")

def main():
    produits = charger_produits("produits.txt")  # Charger depuis un fichier texte
    
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            afficher_produits(produits)
        elif choix == "2":
            ajouter_produit(produits)
        elif choix == "3":
            supprimer_produit(produits)
        elif choix == "4":
            rechercher_produit(produits)
        elif choix == "5":
            trier_produits(produits)
        elif choix == "6":
            sauvegarder_produits("produits.txt", produits)
            print("À bientôt !")
            break
        else:
            print("Choix invalide, essayez encore.")

if __name__ == "__main__":
    main()
