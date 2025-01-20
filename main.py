from gestion_produits import GestionProduits
from gestion_utilisateurs import GestionUtilisateurs
from interface import InterfaceGraphique


def main():
    gestion_utilisateurs = GestionUtilisateurs()
    app = InterfaceGraphique(gestion_utilisateurs, None)
    app.run()


if __name__ == "__main__":
    main()
