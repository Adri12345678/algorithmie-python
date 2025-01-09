import tkinter as tk
from tkinter import messagebox
from gestion_produits import GestionProduits
from gestion_utilisateurs import GestionUtilisateurs
import matplotlib.pyplot as plt

class InterfaceGraphique:
    def __init__(self, gestion_utilisateurs, gestion_produits, utilisateur='produits_Adrien.csv'):
        self.gestion_utilisateurs = gestion_utilisateurs
        self.gestion_produits = gestion_produits
        self.utilisateur = utilisateur

        # Configuration de la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Gestionnaire Utilisateurs & Produits")
        self.root.geometry("600x400")

        # Charger l'écran d'accueil
        self.ecran_accueil()

    def ecran_accueil(self):
        # Effacer l'écran actuel
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets pour l'écran d'accueil
        label = tk.Label(self.root, text="Bienvenue dans le Gestionnaire", font=("Helvetica", 18))
        label.pack(pady=20)

        bouton_identification = tk.Button(
            self.root, text="S'identifier", command=self.ecran_identification
        )
        bouton_identification.pack(pady=10)

        bouton_inscription = tk.Button(
            self.root, text="S'inscrire", command=self.ecran_inscription
        )
        bouton_inscription.pack(pady=10)

        bouton_quitter = tk.Button(
            self.root, text="Quitter", command=self.root.quit
        )
        bouton_quitter.pack(pady=10)

    def ecran_identification(self):
        # Effacer l'écran actuel
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets pour l'écran d'identification
        label = tk.Label(self.root, text="S'identifier", font=("Helvetica", 16))
        label.pack(pady=20)

        tk.Label(self.root, text="Nom d'utilisateur:").pack(pady=5)
        entry_nom = tk.Entry(self.root)
        entry_nom.pack(pady=5)
        self.utilisateur = entry_nom.get()

        tk.Label(self.root, text="Mot de passe:").pack(pady=5)
        entry_mdp = tk.Entry(self.root, show="*")
        entry_mdp.pack(pady=5)

        def verifier_identification():
            nom = entry_nom.get()
            mot_de_passe = entry_mdp.get()
            if self.gestion_utilisateurs.verifier_utilisateur(nom, mot_de_passe):
                if nom == "admin":
                    self.menu_admin()
                else:
                    self.menu_utilisateur(nom)
            else:
                messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

        bouton_verifier = tk.Button(self.root, text="Se connecter", command=verifier_identification)
        bouton_verifier.pack(pady=10)

        bouton_retour = tk.Button(self.root, text="Retour", command=self.ecran_accueil)
        bouton_retour.pack(pady=10)

    def ecran_inscription(self):
        # Effacer l'écran actuel
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets pour l'écran d'inscription
        label = tk.Label(self.root, text="S'inscrire", font=("Helvetica", 16))
        label.pack(pady=20)

        tk.Label(self.root, text="Nom d'utilisateur:").pack(pady=5)
        entry_nom = tk.Entry(self.root)
        entry_nom.pack(pady=5)

        tk.Label(self.root, text="Mot de passe:").pack(pady=5)
        entry_mdp = tk.Entry(self.root, show="*")
        entry_mdp.pack(pady=5)

        def enregistrer_utilisateur():
            nom = entry_nom.get()
            mot_de_passe = entry_mdp.get()
            if nom and mot_de_passe:
                self.gestion_utilisateurs.ajouter_utilisateur_interface(nom, mot_de_passe)
                messagebox.showinfo("Succès", f"Utilisateur '{nom}' ajouté avec succès.")
                self.ecran_accueil()
            else:
                messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

        bouton_enregistrer = tk.Button(self.root, text="S'inscrire", command=enregistrer_utilisateur)
        bouton_enregistrer.pack(pady=10)

        bouton_retour = tk.Button(self.root, text="Retour", command=self.ecran_accueil)
        bouton_retour.pack(pady=10)

    def menu_admin(self):
        # Effacer l'écran actuel
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets pour le menu admin
        label = tk.Label(self.root, text="Menu Administrateur", font=("Helvetica", 16))
        label.pack(pady=20)

        bouton_afficher_utilisateurs = tk.Button(
            self.root, text="Afficher les utilisateurs", command=self.afficher_utilisateurs
        )
        bouton_afficher_utilisateurs.pack(pady=10)

        bouton_supprimer_utilisateur = tk.Button(
            self.root, text="Supprimer un utilisateur", command=self.supprimer_utilisateur
        )
        bouton_supprimer_utilisateur.pack(pady=10)

        bouton_retour = tk.Button(self.root, text="Retour", command=self.ecran_accueil)
        bouton_retour.pack(pady=10)

    def menu_utilisateur(self, nom_utilisateur):
        # Effacer l'écran actuel
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets pour le menu utilisateur
        label = tk.Label(self.root, text=f"Bienvenue, {nom_utilisateur}", font=("Helvetica", 16))
        label.pack(pady=20)

        bouton_afficher_produits = tk.Button(
            self.root, text="Afficher vos produits", command=self.afficher_produits
        )
        bouton_afficher_produits.pack(pady=10)

        bouton_trier_produits = tk.Button(
            self.root, text="Trier vos produits", command=self.trier_produits
        )
        bouton_trier_produits.pack(pady=10)

        bouton_retour = tk.Button(self.root, text="Retour", command=self.ecran_accueil)
        bouton_retour.pack(pady=10)

    def afficher_utilisateurs(self):
        utilisateurs = [u["nom_utilisateur"] for u in self.gestion_utilisateurs.utilisateurs]
        message = "Liste des utilisateurs:\n" + "\n".join(utilisateurs)
        messagebox.showinfo("Utilisateurs", message)

    def supprimer_utilisateur(self):
        # Effacer l'écran actuel
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets pour la suppression d'utilisateur
        label = tk.Label(self.root, text="Supprimer un utilisateur", font=("Helvetica", 16))
        label.pack(pady=20)

        tk.Label(self.root, text="Nom d'utilisateur à supprimer :").pack(pady=5)
        entry_nom = tk.Entry(self.root)
        entry_nom.pack(pady=5)

        def effectuer_suppression():
            nom = entry_nom.get()
            if self.gestion_utilisateurs.supprimer_utilisateur_console(nom):
                messagebox.showinfo("Succès", f"L'utilisateur '{nom}' a été supprimé.")
            else:
                messagebox.showerror("Erreur", f"L'utilisateur '{nom}' n'existe pas.")
            self.menu_admin()

        bouton_supprimer = tk.Button(self.root, text="Supprimer", command=effectuer_suppression)
        bouton_supprimer.pack(pady=10)

        bouton_retour = tk.Button(self.root, text="Retour", command=self.menu_admin)
        bouton_retour.pack(pady=10)

    def afficher_produits(self):
        # Récupérer les produits de l'utilisateur connecté
        temp = f"produits_{self.utilisateur}.csv"
        produits = self.gestion_produits.produits
        if not produits:
            messagebox.showinfo("Produits", "Aucun produit trouvé.")
            return

        # Afficher les produits dans une fenêtre pop-up
        message = "Liste des produits :\n"
        for produit in produits:
            message += f"{produit['nom']} - Prix: {produit['prix']}€ - Quantité: {produit['quantite']}\n"
        
        messagebox.showinfo("Produits", message)

    def trier_produits(self):
        # Effacer l'écran actuel
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets pour le tri des produits
        label = tk.Label(self.root, text="Trier vos produits", font=("Helvetica", 16))
        label.pack(pady=20)

        def effectuer_tri(critere):
            if critere == "nom":
                self.gestion_produits.produits.sort(key=lambda p: p['nom'])
            elif critere == "prix":
                self.gestion_produits.produits.sort(key=lambda p: p['prix'])
            elif critere == "quantite":
                self.gestion_produits.produits.sort(key=lambda p: p['quantite'])
            self.gestion_produits.enregistrer_produits(self.gestion_produits.produits)
            messagebox.showinfo("Succès", f"Produits triés par {critere}.")
            self.menu_utilisateur(self.gestion_produits.nom_utilisateur)

        bouton_tri_nom = tk.Button(self.root, text="Trier par nom", command=lambda: effectuer_tri("nom"))
        bouton_tri_nom.pack(pady=5)

        bouton_tri_prix = tk.Button(self.root, text="Trier par prix", command=lambda: effectuer_tri("prix"))
        bouton_tri_prix.pack(pady=5)

        bouton_tri_quantite = tk.Button(self.root, text="Trier par quantité", command=lambda: effectuer_tri("quantite"))
        bouton_tri_quantite.pack(pady=5)

        bouton_retour = tk.Button(self.root, text="Retour", command=lambda: self.menu_utilisateur(self.gestion_produits.nom_utilisateur))
        bouton_retour.pack(pady=10)

    def run(self):
        self.root.mainloop()


