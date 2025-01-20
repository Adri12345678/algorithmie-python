import tkinter as tk
from tkinter import messagebox, simpledialog
from gestion_utilisateurs import GestionUtilisateurs
from gestion_produits import GestionProduits
import hashlib
import requests


class InterfaceGraphique:
    def __init__(self, gestion_utilisateurs, gestion_produits):
        self.gestion_utilisateurs = gestion_utilisateurs
        self.gestion_produits = gestion_produits
        self.utilisateur_actif = None

        # Créer la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Application de Gestion")
        self.root.geometry("400x300")

    def run(self):
        """Lance l'application graphique."""
        self.page_accueil()
        self.root.mainloop()

    def page_accueil(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Bienvenue !", font=("Helvetica", 20))
        label.pack(pady=20)

        bouton_connexion = tk.Button(self.root, text="Se connecter", font=("Helvetica", 14), command=self.afficher_ecran_connexion)
        bouton_connexion.pack(pady=10)

        bouton_inscription = tk.Button(self.root, text="S'inscrire", font=("Helvetica", 14), command=self.afficher_inscription)
        bouton_inscription.pack(pady=10)


    def afficher_ecran_connexion(self):
        """Affiche l'écran de connexion."""
        self.vider_fenetre()

        tk.Label(self.root, text="Connexion", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Nom d'utilisateur :").pack()
        champ_utilisateur = tk.Entry(self.root)
        champ_utilisateur.pack()

        tk.Label(self.root, text="Mot de passe :").pack()
        champ_mot_de_passe = tk.Entry(self.root, show="*")
        champ_mot_de_passe.pack()

        def connexion():
            nom_utilisateur = champ_utilisateur.get()
            mot_de_passe = champ_mot_de_passe.get()

            if self.gestion_utilisateurs.verifier_utilisateur(nom_utilisateur, mot_de_passe):
                self.utilisateur_actif = nom_utilisateur
                if nom_utilisateur == "admin":
                    self.afficher_menu_admin()
                else:
                    self.gestion_produits = GestionProduits(f"produits_{nom_utilisateur}.csv")
                    self.afficher_menu_utilisateur()
            else:
                messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

        tk.Button(self.root, text="Se connecter", command=connexion).pack(pady=10)

        bouton_retour = tk.Button(self.root, text="Retour", command=self.page_accueil)
        bouton_retour.pack(pady=10)

    def verifier_mot_de_passe_compromis(self, mot_de_passe):
        """Vérifie si un mot de passe est compromis en interrogeant l'API Have I Been Pwned"""
        sha1_hash = hashlib.sha1(mot_de_passe.encode('utf-8')).hexdigest().upper()
        premiers_5 = sha1_hash[:5]
        reste = sha1_hash[5:]

        url = f"https://api.pwnedpasswords.com/range/{premiers_5}"
        response = requests.get(url)

        if response.status_code == 200:
            hash_suffixes = response.text.splitlines()
            for suffix in hash_suffixes:
                if suffix.startswith(reste):
                    return True
            return False
        else:
            print("Erreur lors de la vérification du mot de passe.")
            return False

    def afficher_inscription(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Inscription", font=("Helvetica", 20))
        label.pack(pady=20)

        tk.Label(self.root, text="Nom d'utilisateur :").pack(pady=5)
        entry_nom = tk.Entry(self.root)
        entry_nom.pack(pady=5)

        tk.Label(self.root, text="Mot de passe :").pack(pady=5)
        entry_mdp = tk.Entry(self.root, show="*")
        entry_mdp.pack(pady=5)

        def valider_inscription():
            nom = entry_nom.get()
            mot_de_passe = entry_mdp.get()
            mot_de_passe_est_compromis = self.verifier_mot_de_passe_compromis(mot_de_passe)
            if mot_de_passe_est_compromis:
                messagebox.showerror("Erreur", "Le mot de passe est compromis. Veuillez en choisir un autre.")
                return

            if not nom or not mot_de_passe:
                messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
                return

            if self.gestion_utilisateurs.ajouter_utilisateur(nom, mot_de_passe):
                messagebox.showinfo("Succès", f"Votre mot de passe est sécurisé ! L'utilisateur '{nom}' a été créé !")
                self.page_accueil()
            else:
                messagebox.showerror("Erreur", "Nom d'utilisateur déjà existant.")

        bouton_valider = tk.Button(self.root, text="Valider", command=valider_inscription)
        bouton_valider.pack(pady=10)

        bouton_retour = tk.Button(self.root, text="Retour", command=self.page_accueil)
        bouton_retour.pack(pady=10)


    def afficher_menu_admin(self):
        """Affiche le menu d'administration."""
        self.vider_fenetre()

        tk.Label(self.root, text="Menu Administrateur", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Ajouter un utilisateur", command=self.ajouter_utilisateur).pack(pady=5)
        tk.Button(self.root, text="Supprimer un utilisateur", command=self.supprimer_utilisateur).pack(pady=5)
        tk.Button(self.root, text="Voir la liste des utilisateurs", command=self.afficher_utilisateurs).pack(pady=5)
        tk.Button(self.root, text="Déconnexion", command=self.afficher_ecran_connexion).pack(pady=10)

    def ajouter_utilisateur(self):
        """Ajoute un utilisateur via un dialogue."""
        nom_utilisateur = simpledialog.askstring("Ajouter un utilisateur", "Nom d'utilisateur :")
        mot_de_passe = simpledialog.askstring("Ajouter un utilisateur", "Mot de passe :", show="*")

        if nom_utilisateur and mot_de_passe:
            if self.gestion_utilisateurs.ajouter_utilisateur(nom_utilisateur, mot_de_passe):
                messagebox.showinfo("Succès", f"L'utilisateur '{nom_utilisateur}' a été ajouté.")
            else:
                messagebox.showerror("Erreur", f"L'utilisateur '{nom_utilisateur}' existe déjà.")
        else:
            messagebox.showwarning("Attention", "Les champs ne peuvent pas être vides.")

    def supprimer_utilisateur(self):
        """Supprime un utilisateur via un dialogue."""
        nom_utilisateur = simpledialog.askstring("Supprimer un utilisateur", "Nom d'utilisateur à supprimer :")

        if nom_utilisateur:
            self.gestion_utilisateurs.supprimer_utilisateur(nom_utilisateur)
            messagebox.showinfo("Succès", f"L'utilisateur '{nom_utilisateur}' a été supprimé.")
        else:
            messagebox.showwarning("Attention", "Veuillez entrer un nom d'utilisateur valide.")

    def afficher_utilisateurs(self):
        """Affiche la liste des utilisateurs dans une boîte de dialogue."""
        utilisateurs = self.gestion_utilisateurs.utilisateurs
        liste = "\n".join([u["nom_utilisateur"] for u in utilisateurs])
        messagebox.showinfo("Liste des utilisateurs", liste if liste else "Aucun utilisateur trouvé.")

    def afficher_menu_utilisateur(self):
        """Affiche le menu utilisateur pour gérer les produits."""
        self.vider_fenetre()

        tk.Label(self.root, text=f"Menu Utilisateur - {self.utilisateur_actif}", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Afficher les produits", command=self.afficher_produits).pack(pady=5)
        tk.Button(self.root, text="Ajouter un produit", command=self.ajouter_produit).pack(pady=5)
        tk.Button(self.root, text="Supprimer un produit", command=self.supprimer_produit).pack(pady=5)
        tk.Button(self.root, text="Trier les Produits", command=self.trier_produits).pack(pady=5)
        tk.Button(self.root, text="Afficher les graphes", command=self.afficher_statistiques).pack(pady=5)
        tk.Button(self.root, text="Déconnexion", command=self.afficher_ecran_connexion).pack(pady=10)

    def afficher_produits(self):
        """Affiche la liste des produits dans une boîte de dialogue."""
        produits = self.gestion_produits.produits
        liste = "\n".join([f"{p['nom']} - {p['prix']}€ - {p['quantite']} unités" for p in produits])
        messagebox.showinfo("Liste des produits", liste if liste else "Aucun produit trouvé.")

    def ajouter_produit(self):
        
        def valider_ajout_produit():
            nom = entry_nom.get()
            if not nom:
                messagebox.showwarning("Erreur", "Le nom du produit ne peut pas être vide.")
                return
            prix = entry_prix.get()
            if not prix or not prix.replace('.', '', 1).isdigit():
                messagebox.showwarning("Erreur", "Veuillez entrer un prix valide.")
                return
            quantite = entry_quantite.get()
            if not quantite or not quantite.isdigit():
                messagebox.showwarning("Erreur", "Veuillez entrer une quantité valide.")
                return
            
            # Ajout du produit dans la liste (ou fichier)
            produit = {
                'nom': nom,
                'prix': float(prix),
                'quantite': int(quantite)
            }
            self.gestion_produits.ajouter_produit(nom, prix, quantite)
            messagebox.showinfo("Succès", f"Le produit {nom} a été ajouté.")
            self.menu_utilisateur(self.utilisateur)  # Retour au menu utilisateur après l'ajout
            
            popup.destroy()

        def cancel_ajout():
            popup.destroy()

        popup = tk.Toplevel(self.root)  # Création de la fenêtre pop-up
        popup.title("Ajouter un produit")
        popup.geometry("300x300")

        # Champ pour le nom du produit
        tk.Label(popup, text="Nom du produit :").pack(pady=5)
        entry_nom = tk.Entry(popup)
        entry_nom.pack(pady=5)

        # Champ pour le prix du produit
        tk.Label(popup, text="Prix du produit :").pack(pady=5)
        entry_prix = tk.Entry(popup)
        entry_prix.pack(pady=5)

        # Champ pour la quantité du produit
        tk.Label(popup, text="Quantité du produit :").pack(pady=5)
        entry_quantite = tk.Entry(popup)
        entry_quantite.pack(pady=5)

        # Boutons pour valider ou annuler
        bouton_valider = tk.Button(popup, text="Valider", command=valider_ajout_produit)
        bouton_valider.pack(pady=10)
        bouton_cancel = tk.Button(popup, text="Annuler", command=cancel_ajout)
        bouton_cancel.pack(pady=5)

    def supprimer_produit(self):
        """Supprime un produit via un dialogue."""
        nom = simpledialog.askstring("Supprimer un produit", "Nom du produit à supprimer :")

        if nom:
            self.gestion_produits.supprimer_produit(nom)
            messagebox.showinfo("Succès", f"Produit '{nom}' supprimé avec succès.")
        else:
            messagebox.showwarning("Attention", "Veuillez entrer un nom de produit valide.")

    def trier_produits(self):
        self.fenetre_tri = tk.Toplevel(self.root)
        self.fenetre_tri.title("Trier les Produits")
        self.fenetre_tri.geometry("300x200")

        def trier_par_critere(critere):
            self.gestion_produits.trier_produits(critere)
            if self.gestion_produits.trier_produits(critere):
                messagebox.showinfo("Succès", "Produits triés avec succès.")
            else:
                messagebox.showinfo("Erreur", "Le tri des produits n'as pas aboutit.")
            self.fenetre_tri.destroy()  # Fermer la fenêtre après le tri

        label = tk.Label(self.fenetre_tri, text="Choisissez un critère de tri :")
        label.pack(pady=20)

        bouton_nom = tk.Button(self.fenetre_tri, text="Par Nom", command=lambda: trier_par_critere('nom'))
        bouton_nom.pack(pady=5)

        bouton_prix = tk.Button(self.fenetre_tri, text="Par Prix", command=lambda: trier_par_critere('prix'))
        bouton_prix.pack(pady=5)

        bouton_quantite = tk.Button(self.fenetre_tri, text="Par Quantité", command=lambda: trier_par_critere('quantite'))
        bouton_quantite.pack(pady=5)

    def afficher_statistiques(self):
        """Affiche les statistiques sous forme de graphiques"""
        if self.gestion_produits:
            self.gestion_produits.afficher_statistiques()  # Appelle la méthode des statistiques
        else:
            print("Gestion des produits non initialisée.")

    def vider_fenetre(self):
        """Vide tous les widgets de la fenêtre."""
        for widget in self.root.winfo_children():
            widget.destroy()
