import csv
import matplotlib.pyplot as plt
import pandas as pd

class GestionProduits:
    def __init__(self, fichier_produits):
        self.fichier_produits = fichier_produits
        self.produits = self.charger_produits()
        self.df = pd.read_csv(fichier_produits)

    def charger_produits(self):
        """Charge les produits depuis un fichier CSV."""
        produits = []
        try:
            with open(self.fichier_produits, "r") as fichier:
                lecteur = csv.DictReader(fichier)
                for ligne in lecteur:
                    produits.append({
                        "nom": ligne["nom"],
                        "prix": float(ligne["prix"]),
                        "quantite": int(ligne["quantite"]),
                    })
        except FileNotFoundError:
            pass
        return produits

    def trier_produits(self, critere):
        """
        Trie la liste des produits en fonction du critère spécifié.
        Les critères possibles sont 'nom', 'prix' et 'quantite'.
        """
        if critere == 'nom':
            self.produits.sort(key=lambda produit: produit['nom'])
            self.enregistrer_produits()
            return True
        elif critere == 'prix':
            self.produits.sort(key=lambda produit: produit['prix'])
            self.enregistrer_produits()
            return True
        elif critere == 'quantite':
            self.produits.sort(key=lambda produit: produit['quantite'])
            self.enregistrer_produits()
            return True
        else:
            print(f"Critère de tri '{critere}' non reconnu.")
            return False

    def enregistrer_produits(self):
        """Enregistre les produits dans un fichier CSV."""
        with open(self.fichier_produits, "w", newline="") as fichier:
            champs = ["nom", "prix", "quantite"]
            writer = csv.DictWriter(fichier, fieldnames=champs)
            writer.writeheader()
            writer.writerows(self.produits)

    def ajouter_produit(self, nom, prix, quantite):
        """Ajoute un produit."""
        self.produits.append({
            "nom": nom,
            "prix": prix,
            "quantite": quantite,
        })
        self.enregistrer_produits()

    def supprimer_produit(self, nom):
        """Supprime un produit par son nom."""
        self.produits = [p for p in self.produits if p["nom"] != nom]
        self.enregistrer_produits()

    def afficher_statistiques(self):
        """Affiche les statistiques des produits sous forme de graphiques"""
        # Vérification si les colonnes existent
        if "prix" not in self.df.columns or "quantite" not in self.df.columns:
            print("Les colonnes 'prix' ou 'quantite' sont manquantes dans le fichier.")
            return
        
        # Graphique de la distribution des prix
        plt.figure(figsize=(10, 5))  # Taille du graphique
        plt.subplot(1, 2, 1)  # Placer le graphique à gauche (1 ligne, 2 colonnes)
        plt.hist(self.df["prix"], bins=10, color='blue', alpha=0.7)  # Histogramme des prix
        plt.title("Distribution des prix des produits")
        plt.xlabel("Prix")
        plt.ylabel("Nombre de produits")

        # Graphique de la distribution des quantités
        plt.subplot(1, 2, 2)  # Placer le graphique à droite (1 ligne, 2 colonnes)
        plt.bar(self.df["nom"], self.df["quantite"], color='green', alpha=0.7)  # Bar chart des quantités
        plt.title("Quantité des produits")
        plt.xlabel("Produits")
        plt.ylabel("Quantité")

        plt.tight_layout()  # Ajuste les éléments du graphique pour éviter les chevauchements
        plt.show()  # Affiche le graphique

