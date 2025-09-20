# nettoyeur.py
# v1.2 -- correction bug doublons subtils
#
# Problème découvert en testant avec test_doublons_subtils.csv :
# "Balance analytique" et "Balance Analytique " (avec espace en fin)
# n'étaient PAS détectés comme doublons parce que la comparaison
# était sensible à la casse et aux espaces.
#
# Fix : normaliser chaque cellule avec .strip().lower() avant
# de créer la clé de comparaison.
# On garde la ligne originale pour l'affichage, mais on compare
# la version normalisée. Deux variables : une pour comparer, une pour afficher.

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


def normaliser_ligne(ligne):
    """
    Normalise une ligne pour la comparaison :
    - enlève les espaces en début/fin de chaque cellule (.strip())
    - met tout en minuscules (.lower())
    Retourne un tuple utilisable comme clé de dictionnaire.
    """
    return tuple(cellule.strip().lower() for cellule in ligne)


def detecter_doublons(lignes):
    """
    Détecte les doublons en comparant les lignes normalisées.
    Retourne une liste de tuples : (ligne_originale, nb_occurrences).
    """
    compteur = {}       # clé normalisée -> nombre d'occurrences
    premieres = {}      # clé normalisée -> première ligne originale vue

    for ligne in lignes:
        cle = normaliser_ligne(ligne)

        if cle in compteur:
            compteur[cle] += 1
        else:
            compteur[cle] = 1
            premieres[cle] = ligne

    doublons = []
    for cle, count in compteur.items():
        if count > 1:
            doublons.append((premieres[cle], count))

    return doublons


def afficher_resultats(entete, doublons):
    """Affiche les doublons trouvés dans la console."""
    if len(doublons) == 0:
        print("Aucun doublon trouvé !")
        return

    print(f"{len(doublons)} doublon(s) détecté(s) :\n")
    for ligne_originale, count in doublons:
        print(f"  x{count} occurrences -> {ligne_originale}")


# Point d'entrée
if len(sys.argv) < 2:
    print("Usage : python nettoyeur.py <fichier.csv>")
    sys.exit(1)

chemin = sys.argv[1]
entete, lignes = lire_csv(chemin)
doublons = detecter_doublons(lignes)
afficher_resultats(entete, doublons)
