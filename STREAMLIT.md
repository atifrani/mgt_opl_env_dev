

## Mise en place d'un environnement de développement local:

Avant de pouvoir réellement commencer à créer des applications Streamlit, nous devrons d'abord configurer un environnement de développement.  

### Installer Conda:
* Installez conda en allant sur https://docs.conda.io/en/latest/miniconda.html et choisissez votre système d'exploitation (Windows, Mac ou Linux).
* Téléchargez et exécutez le programme d'installation pour installer conda.

### Créer un nouvel environnement Conda
Maintenant que vous avez installé **conda**, créons un **environnement conda** pour gérer toutes les dépendances de la bibliothèque Python.  

Pour créer un nouvel environnement avec **Python 3.9**, saisissez ce qui suit :  

```
conda create -n stenv python=3.9
```

où **create -n stenv** créera un environnement conda nommé **stenv** et **python=3.9** configurera l'environnement conda avec Python version 3.9.


### Activer l'environnement conda

Pour utiliser un environnement conda que nous venons de créer et qui s'appelle stenv, entrez ce qui suit dans la ligne de commande :  

```
conda activate stenv
```

### Installez la bibliothèque Streamlit

Il est maintenant temps d'installer la bibliothèque streamlit :  

```
pip install streamlit
```

### Lancement de la démo Streamlit

Pour lancer la démo Streamlit (Figure 1), saisissez :

```
streamlit hello
```

### Construire votre première application Streamlit
 
Lancez votre IDE VS Code.

Créez un projet (repertoire) appelé streamlit-project, à l'interieur du projet créez un fichier streamlit_app.py.  

Saisie de vos premières lignes de code dans le fichier nouvellement créé, entrez les lignes de code suivantes :  

```
import streamlit as st

st.write('HelloMBADIA !')
```
Enregistrez le fichier.  

***st.write*** permet d'écrire du texte et des arguments dans l'application Streamlit.  

Lancez le terminal et positonnez vous à l'interieur du projet ou se situe le fichier streamlit, entrez ce qui suit :  

```
streamlit run streamlit_app.py
```

Une fenêtre de navigateur devrait apparaître et afficher l'application Streamlit nouvellement créée.  

***Félicitations !*** Vous venez de créer votre première application Streamlit !  

Retournez sur le terminal et exécuter les commandes suivantes:

```
git status
git add streamlit_app.py
git commit -m 'initial streamlit app'
git push origin main
```


* Une application simple qui affiche des messages différents selon que le bouton ait été pressé ou non.
Déroulement de l'application :  
    * Par défaut, l'application affiche "Goodbye"
    * En cliquant sur le bouton, l'application affiche le message alternatif "Why Hello?"


Copiez les lignes de code suivantes dans votre fichier streamlit_app.py:  

```
import streamlit as st

st.header('st.button')

if st.button('say hello'):
     st.write('why hello?')
else:
     st.write('goodbye')

```
Enregistrez le fichier.   

***st.button** permet l'affichage d'un bouton.

Relancez votre application streamlit si nécessaire:  

```
streamlit run streamlit_app.py
```

Vérifiez le résultat qui s'affiche sur votre navigateur.  

Retournez sur le terminal et exécuter les commandes suivantes:

```
git status
git add streamlit_app.py
git commit -m 'ajout d'un bouton'
git push origin main
```

