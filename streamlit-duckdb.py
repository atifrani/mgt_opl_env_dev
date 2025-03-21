import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import tempfile
import os

# Configuration de la page
st.set_page_config(page_title="Analyse des données du Titanic avec DuckDB", layout="wide")

# Titre de l'application
st.title("Analyse des données du Titanic avec DuckDB et Streamlit")
st.write("Cette application analyse les données des passagers du Titanic en utilisant DuckDB et Streamlit.")

# Fonction pour charger les données de démonstration du Titanic
def charger_donnees_titanic_demo():
    # URL des données Titanic de démonstration
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    return pd.read_csv(url)

# Sidebar pour le chargement des données
st.sidebar.title("Source de données")
source_option = st.sidebar.radio(
    "Choisir la source de données:",
    ["Données Titanic de démonstration", "Télécharger un fichier CSV"]
)

# Initialiser la connexion DuckDB
conn = duckdb.connect(database=':memory:', read_only=False)

# Obtenir les données
if source_option == "Données Titanic de démonstration":
    df = charger_donnees_titanic_demo()
    st.sidebar.success("Données Titanic de démonstration chargées!")
    
    # Enregistrer les données dans DuckDB
    conn.execute("CREATE TABLE IF NOT EXISTS titanic AS SELECT * FROM df")
    
else:
    uploaded_file = st.sidebar.file_uploader("Télécharger un fichier CSV", type=["csv"])
    if uploaded_file is not None:
        # Sauvegarder temporairement le fichier
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # Créer une table à partir du CSV avec DuckDB
        conn.execute(f"CREATE TABLE IF NOT EXISTS titanic AS SELECT * FROM read_csv_auto('{tmp_path}')")
        
        # Charger les données pour affichage
        df = conn.execute("SELECT * FROM titanic").fetchdf()
        st.sidebar.success(f"{len(df)} passagers chargés!")
        
        # Supprimer le fichier temporaire
        os.unlink(tmp_path)
    else:
        st.info("Veuillez télécharger un fichier CSV ou utiliser les données de démonstration.")
        st.stop()

# Afficher un aperçu des données
st.subheader("Aperçu des données")
st.dataframe(df.head(10))

# Statistiques générales
st.header("Statistiques générales")

# Utiliser DuckDB pour les statistiques de survie
stats_generales = conn.execute("""
    SELECT 
        COUNT(*) as total_passagers,
        SUM(Survived) as total_survivants,
        ROUND(SUM(Survived) * 100.0 / COUNT(*), 2) as pourcentage_survie
    FROM titanic
""").fetchdf()

col1, col2, col3 = st.columns(3)
col1.metric("Nombre total de passagers", stats_generales['total_passagers'][0])
col2.metric("Nombre de survivants", stats_generales['total_survivants'][0])
col3.metric("Taux de survie", f"{stats_generales['pourcentage_survie'][0]}%")

# Créer les deux graphiques demandés
st.header("Analyse des survivants")

# 1. Graphique du nombre de survivants par sexe
survivants_par_sexe = conn.execute("""
    SELECT 
        Sex,
        SUM(CASE WHEN Survived = 1 THEN 1 ELSE 0 END) as nombre_survivants,
        SUM(CASE WHEN Survived = 0 THEN 1 ELSE 0 END) as nombre_deces,
        COUNT(*) as total
    FROM titanic
    GROUP BY Sex
    ORDER BY Sex
""").fetchdf()

# 2. Graphique du nombre de survivants par âge
# D'abord, créer des groupes d'âge pour une meilleure visualisation
survivants_par_age = conn.execute("""
    SELECT 
        CASE 
            WHEN Age < 10 THEN '0-9'
            WHEN Age < 20 THEN '10-19'
            WHEN Age < 30 THEN '20-29'
            WHEN Age < 40 THEN '30-39'
            WHEN Age < 50 THEN '40-49'
            WHEN Age < 60 THEN '50-59'
            WHEN Age < 70 THEN '60-69'
            WHEN Age < 80 THEN '70-79'
            WHEN Age IS NULL THEN 'Inconnu'
            ELSE '80+'
        END as groupe_age,
        SUM(CASE WHEN Survived = 1 THEN 1 ELSE 0 END) as nombre_survivants,
        SUM(CASE WHEN Survived = 0 THEN 1 ELSE 0 END) as nombre_deces,
        COUNT(*) as total
    FROM titanic
    GROUP BY groupe_age
    ORDER BY groupe_age
""").fetchdf()

# Afficher les deux graphiques côte à côte
col1, col2 = st.columns(2)

with col1:
    st.subheader("Survivants par sexe")
    
    # Créer un graphique à barres groupées pour les survivants par sexe
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=survivants_par_sexe['Sex'],
        y=survivants_par_sexe['nombre_survivants'],
        name='Survivants',
        marker_color='green'
    ))
    
    fig.add_trace(go.Bar(
        x=survivants_par_sexe['Sex'],
        y=survivants_par_sexe['nombre_deces'],
        name='Décès',
        marker_color='red'
    ))
    
    fig.update_layout(
        barmode='group',
        xaxis_title='Sexe',
        yaxis_title='Nombre de passagers',
        legend_title='Statut'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Ajouter des statistiques
    taux_survie_sexe = conn.execute("""
        SELECT 
            Sex,
            ROUND(SUM(Survived) * 100.0 / COUNT(*), 2) as taux_survie
        FROM titanic
        GROUP BY Sex
    """).fetchdf()
    
    st.write("Taux de survie par sexe:")
    for index, row in taux_survie_sexe.iterrows():
        st.write(f"- {row['Sex']}: {row['taux_survie']}%")

with col2:
    st.subheader("Survivants par groupe d'âge")
    
    # Filtrer les groupes d'âge non-nuls pour un graphique plus clair
    survivants_par_age_filtre = survivants_par_age[survivants_par_age['groupe_age'] != 'Inconnu']
    
    # Créer le graphique à barres empilées pour les survivants par âge
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=survivants_par_age_filtre['groupe_age'],
        y=survivants_par_age_filtre['nombre_survivants'],
        name='Survivants',
        marker_color='green'
    ))
    
    fig.add_trace(go.Bar(
        x=survivants_par_age_filtre['groupe_age'],
        y=survivants_par_age_filtre['nombre_deces'],
        name='Décès',
        marker_color='red'
    ))
    
    fig.update_layout(
        barmode='group',
        xaxis_title='Groupe d\'âge',
        yaxis_title='Nombre de passagers',
        legend_title='Statut',
        xaxis={'categoryorder': 'array', 
               'categoryarray': ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Afficher le taux de survie par groupe d'âge
    taux_survie_age = conn.execute("""
        SELECT 
            CASE 
                WHEN Age < 10 THEN '0-9'
                WHEN Age < 20 THEN '10-19'
                WHEN Age < 30 THEN '20-29'
                WHEN Age < 40 THEN '30-39'
                WHEN Age < 50 THEN '40-49'
                WHEN Age < 60 THEN '50-59'
                WHEN Age < 70 THEN '60-69'
                WHEN Age < 80 THEN '70-79'
                WHEN Age IS NULL THEN 'Inconnu'
                ELSE '80+'
            END as groupe_age,
            ROUND(SUM(Survived) * 100.0 / COUNT(*), 2) as taux_survie
        FROM titanic
        WHERE Age IS NOT NULL
        GROUP BY groupe_age
        ORDER BY groupe_age
    """).fetchdf()
    
    st.write("Taux de survie par groupe d'âge:")
    for index, row in taux_survie_age.iterrows():
        st.write(f"- {row['groupe_age']}: {row['taux_survie']}%")

# Analyse croisée (sexe et âge combinés)
st.header("Analyse croisée des survivants par sexe et âge")

# Créer une requête pour obtenir les données croisées
survivants_sexe_age = conn.execute("""
    SELECT 
        Sex,
        CASE 
            WHEN Age < 10 THEN '0-9'
            WHEN Age < 20 THEN '10-19'
            WHEN Age < 30 THEN '20-29'
            WHEN Age < 40 THEN '30-39'
            WHEN Age < 50 THEN '40-49'
            WHEN Age < 60 THEN '50-59'
            WHEN Age < 70 THEN '60-69'
            WHEN Age < 80 THEN '70-79'
            WHEN Age IS NULL THEN 'Inconnu'
            ELSE '80+'
        END as groupe_age,
        ROUND(SUM(Survived) * 100.0 / COUNT(*), 2) as taux_survie,
        COUNT(*) as total
    FROM titanic
    GROUP BY Sex, groupe_age
    ORDER BY Sex, groupe_age
""").fetchdf()

# Filtrer les données pour exclure les âges inconnus
survivants_sexe_age_filtre = survivants_sexe_age[survivants_sexe_age['groupe_age'] != 'Inconnu']

# Créer le graphique de chaleur (heatmap)
fig = px.density_heatmap(
    survivants_sexe_age_filtre, 
    x='groupe_age', 
    y='Sex', 
    z='taux_survie',
    color_continuous_scale="RdYlGn",
    title="Taux de survie (%) par sexe et groupe d'âge",
    labels={'groupe_age': 'Groupe d\'âge', 'Sex': 'Sexe', 'taux_survie': 'Taux de survie (%)'},
    text_auto=True
)

fig.update_layout(
    xaxis={'categoryorder': 'array', 
           'categoryarray': ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']}
)

st.plotly_chart(fig, use_container_width=True)

# Analyse par classe
st.header("Analyse par classe de voyage")

# Requête pour obtenir les statistiques par classe
stats_classe = conn.execute("""
    SELECT 
        Pclass as classe,
        COUNT(*) as total_passagers,
        SUM(Survived) as total_survivants,
        ROUND(SUM(Survived) * 100.0 / COUNT(*), 2) as pourcentage_survie
    FROM titanic
    GROUP BY classe
    ORDER BY classe
""").fetchdf()

# Créer le graphique
fig = px.bar(
    stats_classe,
    x='classe',
    y='total_passagers',
    color='pourcentage_survie',
    text='pourcentage_survie',
    labels={'classe': 'Classe', 'total_passagers': 'Nombre de passagers', 'pourcentage_survie': 'Taux de survie (%)'},
    title="Taux de survie par classe",
    color_continuous_scale="RdYlGn"
)
fig.update_traces(texttemplate='%{text}%', textposition='outside')

st.plotly_chart(fig, use_container_width=True)


# Exporter les données
st.header("Exporter les données")
if st.button("Exporter les résultats en CSV"):
    csv = conn.execute("SELECT * FROM titanic").fetchdf().to_csv(index=False)
    st.download_button(
        label="Télécharger les données (CSV)",
        data=csv,
        file_name='titanic_analyse.csv',
        mime='text/csv',
    )

# Afficher les informations sur DuckDB
st.sidebar.subheader("À propos de DuckDB")
version_duckdb = conn.execute("SELECT version()").fetchone()[0]
st.sidebar.info(f"Version DuckDB: {version_duckdb}")
st.sidebar.write("DuckDB est un SGBD analytique embarqué optimisé pour l'analyse OLAP.")

# Fermer la connexion DuckDB
conn.close()
