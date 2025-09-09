# Nettoyeur et rapport CSV (Python)

Un script Python pour lire un fichier CSV, détecter les lignes dupliquées
et générer un rapport de ce qui a été trouvé.

J'ai fait ce projet parce que j'avais des exports Excel avec des doublons
et je voulais comprendre comment les détecter automatiquement.
C'est aussi une bonne façon de pratiquer Python sur quelque chose d'utile.

## Ce que ça fait

1. Lit un fichier CSV
2. Détecte les lignes en double (même si la casse ou les espaces diffèrent)
3. Génère un rapport `.txt` et un fichier CSV propre sans doublons

## Utilisation

```bash
python nettoyeur.py mon_fichier.csv
```

Le script crée automatiquement :
- `rapport_[nom_fichier].txt` — résumé lisible
- `rapport_[nom_fichier].csv` — liste des doublons détectés

## Fichiers de test inclus

| Fichier | Description |
|---|---|
| `donnees_test/test_simple.csv` | Doublons évidents (lignes identiques) |
| `donnees_test/test_doublons_subtils.csv` | Doublons avec espaces et majuscules différents |
| `donnees_test/test_propre.csv` | Aucun doublon — pour vérifier les faux positifs |

## Ce que j'ai appris

- Lire et écrire des fichiers CSV avec le module `csv`
- Utiliser un dictionnaire pour détecter les doublons efficacement
- L'importance de `.strip().lower()` — sans ça, "Balance Analytique " et
  "balance analytique" ne sont pas détectés comme doublons
- Écrire un fichier texte de rapport proprement avec `open()` et `write()`
- Passer des arguments à un script avec `sys.argv`

---
*Projet personnel — septembre / octobre 2025*
