import csv
import hashlib

class GestionUtilisateurs:
    def __init__(self, fichier_utilisateurs="utilisateurs.csv"):
        self.fichier_utilisateurs = fichier_utilisateurs
        self.utilisateurs = self.charger_utilisateurs()

    def hacher_mot_de_passe(self, mot_de_passe):
        hachage = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        return hachage

    def charger_utilisateurs(self):
        utilisateurs = []
        try:
            with open(self.fichier_utilisateurs, mode="r") as f:
                lecteur_csv = csv.DictReader(f)
                for ligne in lecteur_csv:
                    utilisateurs.append(ligne)
        except FileNotFoundError:
            print(f"Le fichier {self.fichier_utilisateurs} n'existe pas encore.")
        return utilisateurs

    def supprimer_utilisateur(self, nom_utilisateur):
        self.utilisateurs = [u for u in self.utilisateurs if u['nom_utilisateur'] != nom_utilisateur]
        print(f"Utilisateur '{nom_utilisateur}' supprimé.")
        self.sauvegarder_utilisateurs()

    def verifier_compromis(self, mot_de_passe):
        hachage_mot_de_passe = self.hacher_mot_de_passe(mot_de_passe)
        
        with open("hachages_compromis.csv", mode="r") as f:
            lecteur_csv = csv.reader(f)
            for ligne in lecteur_csv:
                if ligne[1] == hachage_mot_de_passe:
                    return True
        return False

    def ajouter_utilisateur(self, nom_utilisateur, mot_de_passe):
        if self.verifier_compromis(mot_de_passe):
            print("⚠️ Le mot de passe est compromis. Choisissez un autre mot de passe.")
            return  
        
        mot_de_passe_hache = self.hacher_mot_de_passe(mot_de_passe)
        self.utilisateurs.append({"nom_utilisateur": nom_utilisateur, "mot_de_passe": mot_de_passe_hache})
        print(f"Utilisateur '{nom_utilisateur}' ajouté avec succès.")
        
        self.sauvegarder_utilisateurs()

    def sauvegarder_utilisateurs(self):
        with open(self.fichier_utilisateurs, mode="w", newline="") as f:
            champs = ["nom_utilisateur", "mot_de_passe"]
            ecrivain_csv = csv.DictWriter(f, fieldnames=champs)
            ecrivain_csv.writeheader()
            ecrivain_csv.writerows(self.utilisateurs)
