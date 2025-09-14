# nettoyeur.py
# Lecture d'un CSV + détection des lignes dupliquées
# v1.1 -- ajout de la détection de doublons
#
# Idée : convertir chaque ligne en tuple et utiliser un dictionnaire
# pour compter combien de fois chaque ligne apparaît.
# Si une ligne apparaît plus d'une fois -> doublon.

import csv
import sys


def lire_csv(chemin_fichier):
    """Lit un fichier CSV, retourne l'en-tête et les lignes séparément."""
    lignes = []
    entete = None

    with open(chemin_fichier, newline='', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        for i, ligne in enumerate(lecteur):
            if i == 0:
                entete = ligne
            else:
                lignes.append(ligne)

    return entete, lignes


def detecter_doublons(lignes):
    """
    Retourne un dictionnaire des lignes qui apparaissent plus d'une fois.
    La clé est un tuple de la ligne, la valeur est le nombre d'occurrences.
    """
    compteur = {}

    for ligne in lignes:
        # Convertir la liste en tuple pour pouvoir l'utiliser comme clé
        cle = tuple(ligne)

        if cle in compteur:
            compteur[cle] += 1
        else:
            compteur[cle] = 1

    # Garder seulement les lignes qui apparaissent plus d'une fois
    doublons = {}
    for cle, count in compteur.items():
        if count > 1:
            doublons[cle] = count

    return doublons


def afficher_resultats(entete, doublons):
    """Affiche les doublons trouvés dans la console."""
    if len(doublons) == 0:
        print("Aucun doublon trouvé !")
        return

    print(f"{len(doublons)} doublon(s) détecté(s) :\n")
    print(f"  En-tête : {entete}")
    print("-" * 50)

    for ligne, count in doublons.items():
        print(f"  x{count} fois -> {list(ligne)}")


# Point d'entrée
if len(sys.argv) < 2:
    print("Usage : python nettoyeur.py <fichier.csv>")
    sys.exit(1)

chemin = sys.argv[1]
entete, lignes = lire_csv(chemin)
doublons = detecter_doublons(lignes)
afficher_resultats(entete, doublons)
