import csv
import hashlib


class GestionUtilisateurs:
    def __init__(self, fichier_utilisateurs="utilisateurs.csv"):
        self.fichier_utilisateurs = fichier_utilisateurs
        self.utilisateurs = self.charger_utilisateurs()

    def charger_utilisateurs(self):
        """Charge les utilisateurs depuis un fichier CSV."""
        utilisateurs = []
        try:
            with open(self.fichier_utilisateurs, "r") as fichier:
                lecteur = csv.DictReader(fichier)
                for ligne in lecteur:
                    utilisateurs.append({
                        "nom_utilisateur": ligne["nom_utilisateur"],
                        "mot_de_passe": ligne["mot_de_passe"],
                    })
        except FileNotFoundError:
            pass
        return utilisateurs

    def enregistrer_utilisateurs(self):
        """Enregistre les utilisateurs dans un fichier CSV."""
        with open(self.fichier_utilisateurs, "w", newline="") as fichier:
            champs = ["nom_utilisateur", "mot_de_passe"]
            writer = csv.DictWriter(fichier, fieldnames=champs)
            writer.writeheader()
            writer.writerows(self.utilisateurs)

    def ajouter_utilisateur(self, nom_utilisateur, mot_de_passe):
        """Ajoute un utilisateur avec mot de passe hashé."""
        for utilisateur in self.utilisateurs:
            if utilisateur["nom_utilisateur"] == nom_utilisateur:
                return False  # L'utilisateur existe déjà
        hash_mdp = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        self.utilisateurs.append({
            "nom_utilisateur": nom_utilisateur,
            "mot_de_passe": hash_mdp,
        })
        self.enregistrer_utilisateurs()
        return True

    def verifier_utilisateur(self, nom_utilisateur, mot_de_passe):
        """Vérifie si un utilisateur existe et si le mot de passe est correct."""
        hash_mdp = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        for utilisateur in self.utilisateurs:
            if utilisateur["nom_utilisateur"] == nom_utilisateur and utilisateur["mot_de_passe"] == hash_mdp:
                return True
        return False

    def supprimer_utilisateur(self, nom_utilisateur):
        """Supprime un utilisateur s'il existe."""
        self.utilisateurs = [
            u for u in self.utilisateurs if u["nom_utilisateur"] != nom_utilisateur
        ]
        self.enregistrer_utilisateurs()
