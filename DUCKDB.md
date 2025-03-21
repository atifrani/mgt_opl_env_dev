# Introduction à DuckDB

## Qu'est-ce que DuckDB ?
DuckDB est un moteur de base de données relationnel rapide et efficace conçu pour l'analyse de données. Il fonctionne en mémoire et est optimisé pour les requêtes analytiques sur des fichiers plats comme CSV et Parquet. Il se distingue par sa légèreté et sa facilité d'utilisation, notamment en intégrant directement des environnements comme Python et R.

* Système embarqué (comme SQLite) mais optimisé pour l'analyse (comme PostgreSQL)
* Performances exceptionnelles pour les requêtes analytiques
* Installation simple sans configuration serveur
* Intégration facile avec Python, R, Java, etc.
* Lecture directe de fichiers CSV, Parquet, JSON

## Installation de DuckDB
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
db.execute("CREATE TABLE titanic AS SELECT * FROM read_csv_auto('titanic.csv')")
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

