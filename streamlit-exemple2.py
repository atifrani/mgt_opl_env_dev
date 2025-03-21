import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données à partir d'un fichier CSV
st.title("Analyse des Survivants du Titanic")

uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Graphique : Nombre de survivants par sexe
    fig, ax = plt.subplots()
    df.groupby("Sex")['Survived'].sum().plot(kind='bar', ax=ax, color=['blue', 'pink'])
    ax.set_title("Nombre de survivants par sexe")
    ax.set_ylabel("Nombre de survivants")
    st.pyplot(fig)

    # Graphique : Répartition des survivants par âge
    fig, ax = plt.subplots()
    df[df["Survived"] == 1]['Age'].hist(bins=8, ax=ax, color='green', alpha=0.7)
    ax.set_title("Répartition des survivants par âge")
    ax.set_xlabel("Âge")
    ax.set_ylabel("Nombre de survivants")
    st.pyplot(fig)

    st.write("Cette application présente une analyse basique des survivants du Titanic en fonction de l'âge et du sexe.")
