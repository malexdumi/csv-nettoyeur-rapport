# nettoyeur.py
# v1.4 -- export CSV des doublons + fichiers de test ajoutés
#
# Dernière amélioration : en plus du rapport .txt, le script
# génère maintenant un fichier CSV listant uniquement les doublons.
# Utile pour corriger les données dans Excel ensuite.

import csv
import sys
import os
from datetime import datetime


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
    """Normalise une ligne : strip + lowercase sur chaque cellule."""
    return tuple(cellule.strip().lower() for cellule in ligne)


def detecter_doublons(lignes):
    """Détecte les doublons en comparant les lignes normalisées."""
    compteur = {}
    premieres = {}

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


def generer_rapport_txt(chemin_fichier, entete, lignes, doublons):
    """Génère un fichier .txt avec le résumé de l'analyse."""
    nom_base = os.path.splitext(os.path.basename(chemin_fichier))[0]
    chemin_rapport = f"rapport_{nom_base}.txt"

    nb_doublons = sum(count for _, count in doublons)
    nb_lignes_uniques = len(lignes) - nb_doublons + len(doublons)

    with open(chemin_rapport, 'w', encoding='utf-8') as rapport:
        rapport.write("=" * 55 + "\n")
        rapport.write("  RAPPORT D'ANALYSE CSV\n")
        rapport.write("=" * 55 + "\n\n")

        rapport.write(f"Fichier analysé  : {chemin_fichier}\n")
        rapport.write(f"Date d'analyse   : {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        rapport.write("--- RÉSUMÉ ---\n")
        rapport.write(f"Lignes totales   : {len(lignes)}\n")
        rapport.write(f"Doublons trouvés : {len(doublons)} groupe(s)\n")
        rapport.write(f"Lignes en double : {nb_doublons}\n")
        rapport.write(f"Lignes uniques   : {nb_lignes_uniques}\n\n")

        if len(doublons) == 0:
            rapport.write("Aucun doublon détecté — fichier propre.\n")
        else:
            rapport.write("--- DÉTAIL DES DOUBLONS ---\n\n")
            rapport.write(f"  Colonnes : {entete}\n\n")
            for i, (ligne, count) in enumerate(doublons, 1):
                rapport.write(f"  [{i}] Apparaît {count}x : {list(ligne)}\n")

    return chemin_rapport


def exporter_doublons_csv(chemin_fichier, entete, doublons):
    """
    Exporte les doublons dans un fichier CSV séparé.
    Ajoute une colonne 'nb_occurrences' pour faciliter la correction.
    """
    nom_base = os.path.splitext(os.path.basename(chemin_fichier))[0]
    chemin_export = f"doublons_{nom_base}.csv"

    with open(chemin_export, 'w', newline='', encoding='utf-8') as fichier:
        ecrivain = csv.writer(fichier)

        # En-tête avec colonne supplémentaire
        ecrivain.writerow(entete + ['nb_occurrences'])

        for ligne, count in doublons:
            ecrivain.writerow(list(ligne) + [count])

    return chemin_export


# Point d'entrée
if len(sys.argv) < 2:
    print("Usage : python nettoyeur.py <fichier.csv>")
    print("\nExemples avec les fichiers de test :")
    print("  python nettoyeur.py donnees_test/test_simple.csv")
    print("  python nettoyeur.py donnees_test/test_doublons_subtils.csv")
    print("  python nettoyeur.py donnees_test/test_propre.csv")
    sys.exit(1)

chemin = sys.argv[1]

if not os.path.exists(chemin):
    print(f"Erreur : fichier '{chemin}' introuvable.")
    sys.exit(1)

print(f"\nAnalyse de : {chemin}")
print("-" * 40)

entete, lignes = lire_csv(chemin)
doublons = detecter_doublons(lignes)

print(f"Lignes lues      : {len(lignes)}")
print(f"Doublons trouvés : {len(doublons)} groupe(s)")

rapport_txt = generer_rapport_txt(chemin, entete, lignes, doublons)
print(f"Rapport texte    : {rapport_txt}")

if len(doublons) > 0:
    rapport_csv = exporter_doublons_csv(chemin, entete, doublons)
    print(f"Export doublons  : {rapport_csv}")
else:
    print("Aucun fichier CSV généré (pas de doublons).")

print("\nTerminé.")
