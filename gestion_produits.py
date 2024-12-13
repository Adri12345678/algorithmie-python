import csv

class GestionProduits:
    def __init__(self, fichier_csv):
        self.fichier_csv = fichier_csv

    def charger_produits(self):
        produits = []
        with open(self.fichier_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['prix'] = float(row['prix'])  # Convertir le prix en float
                row['quantite'] = int(row['quantite'])  # Convertir la quantité en int
                produits.append(row)
        return produits

    def sauvegarder_produits(self, produits):
        with open(self.fichier_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nom", "prix", "quantite"])
            writer.writeheader()
            writer.writerows(produits)

    def ajouter_produit(self, nom, prix, quantite):
        produits = self.charger_produits()
        produits.append({"nom": nom, "prix": prix, "quantite": quantite})
        self.sauvegarder_produits(produits)
        print(f"Produit '{nom}' ajouté avec succès.")

    def supprimer_produit(self, nom):
        produits = self.charger_produits()
        produits = [p for p in produits if p['nom'] != nom]
        self.sauvegarder_produits(produits)
        print(f"Produit '{nom}' supprimé avec succès.")

    def afficher_produits(self):
        produits = self.charger_produits()
        for p in produits:
            print(f"Nom: {p['nom']}, Prix: {p['prix']}, Quantité: {p['quantite']}")

    def rechercher_produit(self, nom):
        produits = self.charger_produits()
        for p in produits:
            if p['nom'].lower() == nom.lower():
                print(f"Produit trouvé : {p}")
                return
        print("Produit introuvable.")

    def trier_produits(self, critere):
        produits = self.charger_produits()
        if critere == "1":
            produits.sort(key=lambda p: p['prix'])
        elif critere == "2":
            produits.sort(key=lambda p: p['quantite'])
        elif critere == "3":
            produits.sort(key=lambda p: p['nom'].lower())
        self.sauvegarder_produits(produits)
        print("Produits triés avec succès.")
