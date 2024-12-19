import csv
import hashlib
import requests

class GestionUtilisateurs:
    def __init__(self, fichier_utilisateurs="utilisateurs.csv"):
        self.fichier_utilisateurs = fichier_utilisateurs
        self.utilisateurs = self.charger_utilisateurs()

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

    def hacher_mot_de_passe(self, mot_de_passe):
        hachage = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        return hachage

    def ajouter_utilisateur(self):
        nom_utilisateur = input("Entrez le nom d'utilisateur : ")
        mot_de_passe = input("Entrez le mot de passe : ")
        if self.verifier_compromis(mot_de_passe):
            print("⚠️ Le mot de passe est compromis. Choisissez un autre mot de passe.")
            return 
        mot_de_passe_hache = self.hacher_mot_de_passe(mot_de_passe)
        self.utilisateurs.append({"nom_utilisateur": nom_utilisateur, "mot_de_passe": mot_de_passe_hache})
        self.utilisateurs.sort(key=lambda p: p['nom_utilisateur'].lower())
        self.sauvegarder_utilisateurs()
        print(f"Compte '{nom_utilisateur}' créé avec succès.")
        fichier_produits = f"produits_{nom_utilisateur}.csv"
        with open(fichier_produits, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nom", "prix", "quantite"])
            writer.writeheader()
    
    def supprimer_utilisateur(self):
        nom_utilisateur = input("Entrez le nom de l'utilisateur à supprimer : ")
        self.utilisateurs = [u for u in self.utilisateurs if u['nom_utilisateur'] != nom_utilisateur]
        print(f"Utilisateur '{nom_utilisateur}' supprimé.")
        self.sauvegarder_utilisateurs()

    def verifier_utilisateur(self, nom_utilisateur, mot_de_passe):
        mot_de_passe_hache = self.hacher_mot_de_passe(mot_de_passe)
        for utilisateur in self.utilisateurs:
            if utilisateur["nom_utilisateur"] == nom_utilisateur and utilisateur["mot_de_passe"] == mot_de_passe_hache:
                return True
        return False

    def verifier_compromis(self, mot_de_passe):
        """
        Vérifie si un mot de passe est compromis en utilisant l'API Have I Been Pwned.
        Retourne True si compromis, sinon False.
        """
        # Générer le hash SHA-1 du mot de passe
        hash_sha1 = hashlib.sha1(mot_de_passe.encode('utf-8')).hexdigest().upper()

        # k-Anonymity : Envoi uniquement les 5 premiers caractères du hash
        prefix = hash_sha1[:5]
        suffix = hash_sha1[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Parcours des résultats retournés
                hashes = response.text.splitlines()
                for h in hashes:
                    h_suffix, count = h.split(':')
                    if h_suffix == suffix:
                        return True
                return False
            else:
                print(f"Erreur lors de la requête à l'API HIBP : {response.status_code}")
                return False
        except Exception as e:
            print(f"Erreur de connexion à l'API HIBP : {e}")
            return False
    
    def afficher_utilisateurs(self):
        self.utilisateurs.sort(key=lambda p: p['nom_utilisateur'].lower())
        self.sauvegarder_utilisateurs()
        print("Liste des utilisateurs :")
        for utilisateur in self.utilisateurs:
            print(f"- {utilisateur['nom_utilisateur']}")
    
    def sauvegarder_utilisateurs(self):
        with open(self.fichier_utilisateurs, mode="w", newline="") as f:
            champs = ["nom_utilisateur", "mot_de_passe"]
            ecrivain_csv = csv.DictWriter(f, fieldnames=champs)
            ecrivain_csv.writeheader()
            ecrivain_csv.writerows(self.utilisateurs)
