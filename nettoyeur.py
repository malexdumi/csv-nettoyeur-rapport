# nettoyeur.py
# Lecture basique d'un fichier CSV et affichage du contenu
# -- Maria-Alexandra, septembre 2025
#
# Premier essai : juste lire le fichier et afficher les lignes.
# Je voulais comprendre comment fonctionne le module csv avant
# d'ajouter la détection de doublons.

import csv
import sys


def lire_csv(chemin_fichier):
    """Lit un fichier CSV et retourne les lignes sous forme de liste."""
    lignes = []

    with open(chemin_fichier, newline='', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            lignes.append(ligne)

    return lignes


def afficher_apercu(lignes):
    """Affiche les 5 premières lignes pour vérifier que la lecture est correcte."""
    print(f"Fichier lu : {len(lignes)} lignes au total (en-tête inclus)\n")
    print("Aperçu des 5 premières lignes :")
    print("-" * 40)

    for i, ligne in enumerate(lignes[:6]):
        if i == 0:
            print(f"EN-TÊTE : {ligne}")
        else:
            print(f"  Ligne {i} : {ligne}")


# Point d'entrée du script
if len(sys.argv) < 2:
    print("Usage : python nettoyeur.py <fichier.csv>")
    sys.exit(1)

chemin = sys.argv[1]
lignes = lire_csv(chemin)
afficher_apercu(lignes)
