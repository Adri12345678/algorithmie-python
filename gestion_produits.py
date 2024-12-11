import os

def charger_produits(fichier):
    if not os.path.exists(fichier):
        return []
    with open(fichier, "r") as f:
        return [eval(ligne.strip()) for ligne in f.readlines()]

def sauvegarder_produits(fichier, produits):
    with open(fichier, "w") as f:
        for produit in produits:
            f.write(f"{produit}\n")

def afficher_produits(produits):
    if not produits:
        print("Aucun produit disponible.")
    else:
        for produit in produits:
            print(f"Nom : {produit['nom']}, Prix : {produit['prix']}, Quantité : {produit['quantite']}")

def ajouter_produit(produits):
    nom = input("Nom du produit : ")
    prix = float(input("Prix du produit : "))
    quantite = int(input("Quantité : "))
    produits.append({"nom": nom, "prix": prix, "quantite": quantite})
    print(f"Produit '{nom}' ajouté avec succès !")

def supprimer_produit(produits):
    nom = input("Nom du produit à supprimer : ")
    for produit in produits:
        if produit['nom'].lower() == nom.lower():
            produits.remove(produit)
            print(f"Produit '{nom}' supprimé.")
            return
    print(f"Produit '{nom}' non trouvé.")

def rechercher_produit(produits):
    nom = input("Nom du produit à rechercher : ")
    for produit in produits:
        if produit['nom'].lower() == nom.lower():
            print(f"Produit trouvé : {produit}")
            return
    print(f"Produit '{nom}' non trouvé.")

def trier_produits(produits):
    print("1. Trier par prix (croissant)")
    print("2. Trier par quantité (croissant)")
    choix = input("Choisissez une option de tri : ")
    
    if choix == "1":
        produits.sort(key=lambda x: x['prix'])
        print("Liste triée par prix.")
    elif choix == "2":
        produits.sort(key=lambda x: x['quantite'])
        print("Liste triée par quantité.")
    else:
        print("Choix invalide.")
