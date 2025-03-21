import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Génération de données fictives
data = {
    "PassengerId": list(range(1, 11)),
    "Survived": [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    "Pclass": [2, 3, 1, 2, 1, 1, 3, 3, 2, 3],
    "Name": [f"Passenger {i}" for i in range(1, 11)],
    "Sex": ["female", "female", "female", "female", "male", "female", "male", "male", "female", "male"],
    "Age": [51, 6, 57, 70, 80, 21, 4, 24, 61, 33],
    "SibSp": [0, 3, 1, 3, 1, 2, 2, 0, 2, 1],
    "Parch": [0, 2, 0, 2, 2, 2, 2, 2, 0, 1],
    "Ticket": ["31721", "90683", "39091", "47302", "13173", "91712", "25863", "14532", "66875", "99259"],
    "Fare": [79.59, 40.29, 32.69, 49.74, 32.69, 67.23, 78.15, 16.79, 60.54, 86.93],
    "Cabin": ["D", "D", "B", "D", "None", "A", "G", "B", "G", "None"],
    "Embarked": ["S", "S", "C", "S", "C", "Q", "S", "Q", "C", "C"]
}

df = pd.DataFrame(data)

# Configuration de l'application Streamlit
st.title("Analyse des Survivants du Titanic")

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
