# Fichiers de test

Trois fichiers CSV pour tester le script dans différentes situations.
Les données sont fictives mais inspirées d'un inventaire de laboratoire
(équipements d'analyse environnementale).

## test_simple.csv
Contient 3 doublons évidents — lignes exactement identiques.
Attendu : 3 groupes de doublons détectés.

```bash
python nettoyeur.py donnees_test/test_simple.csv
```

## test_doublons_subtils.csv
Mêmes doublons mais avec des différences de casse et d'espaces.
Ex: "Balance analytique" vs "Balance Analytique " vs "balance analytique"
Ce fichier sert à tester la normalisation (.strip().lower()).
Attendu : 3 groupes de doublons détectés (mêmes qu'au-dessus).

```bash
python nettoyeur.py donnees_test/test_doublons_subtils.csv
```

## test_propre.csv
Aucun doublon. Sert à vérifier que le script ne génère pas
de faux positifs sur un fichier propre.
Attendu : 0 doublon détecté.

```bash
python nettoyeur.py donnees_test/test_propre.csv
```
