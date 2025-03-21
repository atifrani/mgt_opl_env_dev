import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Chargement des données à partir d'un fichier CSV
st.title("Analyse des Survivants du Titanic")

uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Graphique : Nombre de survivants par sexe sous forme de camembert
    fig, ax = plt.subplots()
    df[df["Survived"] == 1]['Sex'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'pink'], ax=ax)
    ax.set_ylabel("")
    ax.set_title("Répartition des survivants par sexe")
    st.pyplot(fig)

    # Graphique : Répartition des survivants par âge sous forme d'histogramme avec différentes couleurs
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    age_labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90"]
    colors = plt.cm.Paired(np.linspace(0, 1, len(age_labels)))
    
    fig, ax = plt.subplots()
    for i in range(len(age_bins) - 1):
        subset = df[(df["Survived"] == 1) & (df["Age"] >= age_bins[i]) & (df["Age"] < age_bins[i+1])]
        ax.hist(subset["Age"], bins=[age_bins[i], age_bins[i+1]], color=colors[i], alpha=0.7, edgecolor='black', label=age_labels[i])
    
    ax.set_title("Répartition des survivants par âge")
    ax.set_xlabel("Âge")
    ax.set_ylabel("Nombre de survivants")
    ax.legend(title="Tranches d'âge")
    st.pyplot(fig)

    st.write("Cette application présente une analyse basique des survivants du Titanic en fonction de l'âge et du sexe.")
