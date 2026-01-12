# Introduction à DuckDB

## Qu'est-ce que DuckDB ?
DuckDB est un moteur de base de données relationnel rapide et efficace conçu pour l'analyse de données. Il fonctionne en mémoire et est optimisé pour les requêtes analytiques sur des fichiers plats comme CSV et Parquet. Il se distingue par sa légèreté et sa facilité d'utilisation, notamment en intégrant directement des environnements comme Python et R.

* Système embarqué (comme SQLite) mais optimisé pour l'analyse (comme PostgreSQL)
* Performances exceptionnelles pour les requêtes analytiques
* Installation simple sans configuration serveur
* Intégration facile avec Python, R, Java, etc.
* Lecture directe de fichiers CSV, Parquet, JSON


## Installation de DuckDB CLI sur Windows et macOS
Voici comment installer l'interface en ligne de commande (CLI) de DuckDB sur Windows et macOS:
# Installation sur Windows
1. Rendez-vous sur le site officiel de DuckDB: https://duckdb.org/docs/installation/
2. Téléchargez la version Windows appropriée (32 ou 64 bits)
3. Extrayez le fichier zip téléchargé
4. Le fichier exécutable duckdb.exe peut être utilisé directement depuis la ligne de commande

## Installation sur macOS
1. Visitez https://duckdb.org/docs/installation/
2. Téléchargez la version macOS
3. Extrayez l'archive
4. Déplacez l'exécutable dans un répertoire de votre PATH (optionnel)

```
sudo mv duckdb /usr/local/bin/
```

## Vérification de l'installation
Pour vérifier que DuckDB CLI est correctement installé, ouvrez un terminal (Command Prompt ou PowerShell sur Windows, Terminal sur macOS) et tapez:

```
duckdb
```

## Utilisation basique du CLI
Une fois dans l'interface CLI, vous pouvez exécuter des commandes SQL, par exemple:
```
-- Créer une table
CREATE TABLE test (id INTEGER, nom VARCHAR);

-- Insérer des données
INSERT INTO test VALUES (1, 'Test');

-- Interroger les données
SELECT * FROM test;

-- Quitter
.quit
```

## Utilisation avec des fichiers externes
DuckDB CLI peut lire directement des fichiers CSV, Parquet, etc.:
```
-- Lire un CSV
SELECT * FROM read_csv_auto('data/titanic.csv');

-- Créer une table en important les données du CSV
CREATE TABLE titanic AS 
SELECT * FROM read_csv_auto('data/titanic.csv');

-- Vérifier que la table a été créée
SELECT * FROM titanic;
```

## Installation de DuckDB avec Python
Pour utiliser DuckDB avec Python, installez-le via pip :

```sh
pip install duckdb
```

## Chargement et manipulation de données avec DuckDB

### Importation de DuckDB
```python
import duckdb
```

### Création d'une base en mémoire et exécution de requêtes
```python
db = duckdb.connect(database=':memory:')
db.execute("CREATE TABLE people (id INTEGER, name TEXT, age INTEGER)")
db.execute("INSERT INTO people VALUES (1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)")
result = db.execute("SELECT * FROM people").fetchall()
print(result)
```

### Lecture d'un fichier CSV
```python
db.execute("CREATE TABLE titanic AS SELECT * FROM read_csv_auto('data/titanic.csv')")
result = db.execute("SELECT COUNT(*) FROM titanic").fetchall()
print(result)
```

### Requêtes avancées
```python
query = """
SELECT Sex, COUNT(*) AS survivors
FROM titanic
WHERE Survived = 1
GROUP BY Sex
"""
result = db.execute(query).fetchdf()
print(result)
```

## Intégration avec Pandas
DuckDB fonctionne très bien avec Pandas, ce qui facilite l'analyse de données :

```python
import pandas as pd

# Charger un DataFrame Pandas dans DuckDB
df = pd.read_csv("titanic.csv")
db.register("titanic_df", df)

# Exécuter une requête SQL sur le DataFrame
query = "SELECT Pclass, COUNT(*) FROM titanic_df GROUP BY Pclass"
result = db.execute(query).fetchdf()
print(result)


# Fermer la connexion
db.close()
```




## Conclusion
DuckDB est un excellent choix pour analyser de grandes quantités de données directement depuis des fichiers CSV ou Parquet, tout en offrant une intégration fluide avec Python et Pandas. Il est rapide, simple à utiliser et idéal pour les charges de travail analytiques.

