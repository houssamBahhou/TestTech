# Test technique Data Engineering
## Auteur: Houssam BAHHOU
#

## Environnement technique:
#
Le test est fait sur `Windows 10` et `SQL Server 2019`, sur un environnement virtuel de `python (version 3.9.0)`.

Les packages à installer sont dans le fichier `requirements.txt` 

## Contenu:
#
- Le répertoire `data` contient 2 fichiers utilisés pour ce test:
    - `lieux.csv`: où chaque ligne contient une commune, son département et sa région.
    - `personnes.csv`: où chaque ligne contient un nom, un prénom, une date et une commune de naissance.
    - `exemple_resultat.json`: exemple de fichier de sortie.
- Le répertoire `results` contient les 2 fichiers json de sortie:
    - `departements.json`
    - `regions.json`

- `createTables.sql`: Fichier sql de création de la base de données avec les tables `lieux` et `people` sur SQL Server (`Rendu 1`) 
- `ingestion.py`: Script du processus d'ingestion de données (`Rendu 2`)
- `getResult.py`: Script de génération de résultats sous forme de fichiers JSON (`Rendu 3`)
-`AllCodeNotebook.ipynb`: un notebook regroupant l'ensemble du code pour les rendus 2 et 3


## Notes:
#
- Il y a une confusion dans les données. En effet, il existe deux communes avec le même nom `Saint-Denis` (une dans le département `La Réunion` et l'autre dans le département `Seine-Saint-Denis`), ainsi pour une personne avec `Saint-Denis` comme commune de naissance, on ne sera pas capables de déterminer son département de naissance (voire la région), par la suite on ne peut pas avoir le nombre correcte des personnes nées dans ces deux départements.
