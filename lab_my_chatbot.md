## 🎯 Objectif

Concevoir une application web de type **ChatGPT** avec :

- **Streamlit**
- Hébergée via **Streamlit in Snowflake**
- Utilisant **Snowflake Cortex** pour interagir avec un LLM supporté par Cortex
- **Sans utiliser de clé OpenAI**

** Pour activer le model LLM sur votre compte snowflake**

```
SHOW PARAMETERS LIKE 'CORTEX_ENABLED_CROSS_REGION' IN ACCOUNT;

ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'ANY_REGION';

```
L’application devra permettre à un utilisateur de discuter avec un modèle LLM directement depuis l’interface Streamlit déployée dans Snowflake.

## 🧱 Contexte et prérequis

Les étudiants doivent disposer :

- D’un compte Snowflake avec :
  - Accès à un **WAREHOUSE**
  - Droits de création de **DATABASE** et **SCHEMA**
  - Accès à **Streamlit in Snowflake**
  - Accès aux fonctionnalités **Snowflake Cortex**
- Connaissances en :
  - Python
  - Streamlit
  - SQL de base
  - Notions de LLM et prompt engineering


# 📌 Travail demandé


## Partie A — Mise en place de l’environnement Snowflake

1. Créer ou utiliser :
   - Un **WAREHOUSE** (ex : `WH_LAB`)
   - Une **DATABASE** (ex : `DB_LAB`)
   - Un **SCHEMA** (ex : `CHAT_APP`)

2. Vérifier l’accès :
   - Streamlit in Snowflake
   - Snowflake Cortex

3. Créer une application **Streamlit in Snowflake**.

### ✅ Livrable A
- Script SQL de création/configuration
- Capture confirmant la création de l’application Streamlit

---

## Partie B — Développement de l’interface Chat

Développer une interface de type ChatGPT comprenant :

### 1. Interface principale
- Un titre
- Une description courte
- Une zone d’affichage des messages
- Une zone de saisie utilisateur (`st.chat_input`)

### 2. Sidebar
- Sélecteur de modèle Cortex (liste déroulante)
- Slider `temperature` (0.0 – 1.5)
- Bouton **Nouveau Chat**

### 3. Gestion de l’état
- Utilisation de `st.session_state`
- Stockage des messages sous forme :
  ```python
  {"role": "user/assistant/system", "content": "..."}

* Ne pas afficher le message `system` dans l’interface

### ✅ Livrable B

* Code Streamlit fonctionnel
* Interface conversationnelle opérationnelle


## Partie C — Intégration Snowflake Cortex

L’application doit :

1. Construire un prompt basé sur :

   * L’historique de conversation
   * Une instruction système (ex : “Tu es un assistant utile.”)

2. Appeler un **LLM supporté par Snowflake Cortex**

3. Transmettre :

   * Le modèle sélectionné
   * La température
   * Le prompt complet

4. Afficher la réponse générée

⚠️ Contraintes :

* Aucun usage de clé OpenAI
* L’appel doit être fait via Snowflake (SQL ou Snowpark)
* Le modèle doit être supporté par Cortex

### ✅ Livrable C

* Code démontrant l’appel à Cortex
* Réponse générée affichée dans le chat


## Partie D — Persistance

Créer une table Snowflake :

```sql
conversation_id STRING,
timestamp TIMESTAMP,
role STRING,
content STRING
```

Fonctionnalités attendues :

* Génération d’un `conversation_id`
* Insertion des messages dans la table
* (Optionnel) Rechargement d’une conversation existante

### ✅ Livrable D

* Script SQL de création de table
* Code d’insertion
* (Optionnel) Fonction de reload


# 📦 Livrables attendus (final)

Les étudiants doivent fournir :

## 1️⃣ Application Streamlit

* Lien vers l’application déployée
* Capture d’écran fonctionnelle
* Description de l’architecture (Streamlit + Cortex + Snowflake)

## 2️⃣ Code source

* Code Python complet
* Scripts SQL
* Gestion des paramètres
* Commentaires dans le code

## 3️⃣ Repository GitHub Public (OBLIGATOIRE)

Le projet doit être documenté dans un **repository GitHub public** contenant :

### README structuré incluant :

* Description du projet
* Architecture technique
* Étapes de déploiement
* Intégration avec Snowflake Cortex
* Choix du modèle
* Gestion de l’historique
* Instructions d’exécution
* Réponses aux questions de validation

### Exigences du repository :

* Repository public
* Arborescence claire
* Code propre et commenté
* Documentation suffisante pour reproduction

## 4️⃣ Soumission

Les étudiants doivent envoyer le **lien du repository GitHub public** à :

**[axel@logbrain.fr](mailto:axel@logbrain.fr)**

# 📊 Critères d’évaluation

| Critère               | Attendu                          |
| --------------------- | -------------------------------- |
| Interface utilisateur | Ergonomique et claire            |
| Gestion d’état        | Historique fonctionnel           |
| Intégration Cortex    | Appel correct au LLM             |
| Robustesse            | Gestion des erreurs              |
| Documentation         | README clair et reproductible    |
| Qualité GitHub        | Organisation et bonnes pratiques |
| Reproductibilité      | Projet relançable facilement     |

# 🧠 Questions de validation

Les étudiants doivent répondre dans le README :

1. Quel modèle Cortex avez-vous utilisé et pourquoi ?
2. Comment gérez-vous la taille de l’historique ?
3. Comment avez-vous construit le prompt ?
4. Quelles difficultés techniques avez-vous rencontrées ?
5. Comment garantir la confidentialité des conversations stockées ?

# ⭐ Bonus (facultatif)

* Implémentation d’un mini-RAG
* Streaming de la réponse
* Export conversation en JSON/CSV
* Gestion multi-utilisateur
* Ajout d’un système de logs

## Résultat attendu

Une application conversationnelle complète :

* Hébergée sur Snowflake
* Connectée à Snowflake Cortex
* Documentée professionnellement
* Déployable et reproductible
