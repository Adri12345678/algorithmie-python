import csv

class GestionProduits:
    def __init__(self, fichier_csv):
        self.fichier_csv = fichier_csv
        self.produits = self.charger_produits()

    def charger_produits(self):
        produits = []
        with open(self.fichier_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['prix'] = float(row['prix']) 
                row['quantite'] = int(row['quantite'])  
                produits.append(row)
        return produits

    def enregistrer_produits(self, produits):
        with open(self.fichier_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nom", "prix", "quantite"])
            writer.writeheader()
            writer.writerows(produits)

    def ajouter_produit(self):
        nom = input("Nom du produit : ")
        prix = float(input("Prix du produit : "))
        quantite = int(input("Quantité du produit : "))
        self.produits.append({"nom": nom, "prix": prix, "quantite": quantite})
        self.enregistrer_produits(self.produits)
        print(f"Produit '{nom}' ajouté avec succès.")

    def supprimer_produit(self):
        nom = input("Nom du produit à supprimer : ")
        self.produits = [p for p in self.produits if p['nom'] != nom]
        self.enregistrer_produits(self.produits)
        print(f"Produit '{nom}' supprimé avec succès.")

    def rechercher_produit(self):
        nom = input("Nom du produit à rechercher : ")
        for produit in self.produits:
            if produit['nom'] == nom:
                print(f"{produit['nom']} - Prix: {produit['prix']}€ - Quantité: {produit['quantite']}")
                return
        print("Produit non trouvé.")

    def afficher_produits(self):
        for p in self.produits:
            print(f"Nom: {p['nom']}, Prix: {p['prix']}, Quantité: {p['quantite']}")

    def tri_bulles(self):
        print("- prix")
        print("- quantité")
        print("- nom")
        critere = input("Trier par (prix/quantite/nom) : ")
        n = len(self.produits)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.produits[j][critere] > self.produits[j + 1][critere]:
                    self.produits[j], self.produits[j + 1] = self.produits[j + 1], self.produits[j]
        self.enregistrer_produits(self.produits)
        print("Produits triés avec succès.")

    def tri_rapide(self):
        print("1. Trier par prix")
        print("2. Trier par quantité")
        print("3. Trier par nom")
        critere = input("Choisissez un critère de tri : ")
        if critere == "1":
            self.produits.sort(key=lambda p: p['prix'])
        elif critere == "2":
            self.produits.sort(key=lambda p: p['quantite'])
        elif critere == "3":
            self.produits.sort(key=lambda p: p['nom'].lower())
        self.enregistrer_produits(self.produits)
        print("Produits triés avec succès.")

    def recherche_binaire(self):
        self.produits.sort(key=lambda p: p['nom'].lower())
        
        nom = input("Nom du produit à rechercher : ")
        
        bas = 0
        haut = len(self.produits) - 1
        
        while bas <= haut:
            milieu = (bas + haut) // 2
            produit_milieu = self.produits[milieu]
            if produit_milieu['nom'].lower() == nom.lower():
                print(f"{produit_milieu['nom']} - Prix : {produit_milieu['prix']}€ - Quantité : {produit_milieu['quantite']}")
                return produit_milieu
            elif produit_milieu['nom'].lower() < nom.lower():
                bas = milieu + 1
            else:
                haut = milieu - 1
        
        print("Produit non trouvé.")
        return None
