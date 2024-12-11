

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

### Streamlit button:

* Une application simple qui affiche des messages différents selon que le bouton ait été pressé ou non.
Déroulement de l'application :  
    * Par défaut, l'application affiche "Goodbye"
    * En cliquant sur le bouton, l'application affiche le message alternatif "Why Hello?"

```
git branch button     # Créer une nouvelle branch

git branch            # vérifier que la nouvelle branch existe

git checkout button   # se positionner sur la nouvelle branch
```

Créez un nouveau fichier slt_button_app.py Copiez les lignes de code suivantes dans votre fichier slt_button_app.py:  

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
streamlit run slt_button_app.py
```

Vérifiez le résultat qui s'affiche sur votre navigateur.  

Retournez sur le terminal et exécuter les commandes suivantes:

```
git status
git add slt_button_app.py
git commit -m 'ajout d'un bouton'
git push origin button
```

* Fusionner la nouvelle fonctionnalité avec la branch **main**.  

```
git checkout main
git merge button
```

### Streamlit Slider:

Une application simple qui montre les différentes manières d'accepter les entrées de l'utilisateur en ajustant le slider.  

```
git branch slider     # Créer une nouvelle branch

git branch            # vérifier que la nouvelle branch existe

git checkout slider   # se positionner sur la nouvelle branch
```


Créez un nouveau fichier slt_slider_app.py Copiez les lignes de code suivantes dans votre fichier slt_silder_app.py:  

* L'utilisateur sélectionne la valeur en ajustant le slider
* L'application affiche la valeur sélectionnée

```
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 20, 25, 30, 35, 40, 45, 50)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (20.0, 80.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

Enregistrez le fichier.   

**st.slider** permet l'affichage d'un slider.

Relancez votre application streamlit si nécessaire:  

```
streamlit run slt_slider_app.py
```

Vérifiez le résultat qui s'affiche sur votre navigateur.  

Retournez sur le terminal et exécuter les commandes suivantes:

```
git status
git add slt_slider_app.py
git commit -m 'ajout d'un slider'
git push origin slider
```
* Fusionner la nouvelle fonctionnalité avec la branch **main**.  

```
git checkout main
git merge slider
```

### Streamlit Line Chart:

Une application simple pour afficher un graphique linéaire:

Créez un **DataFrame** **Pandas** à partir de nombres générés aléatoirement via **NumPy**.  
Créez et affichez le graphique linéaire via la commande **st.line_chart()**.   

```
git branch linechart     # Créer une nouvelle branch

git branch            # vérifier que la nouvelle branch existe

git checkout linechart   # se positionner sur la nouvelle branch
```

Créez un nouveau fichier slt_linechart_app.py Copiez les lignes de code suivantes dans votre fichier slt_linechart_app.py:  

```
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

chart_data

st.line_chart(chart_data)

```

Enregistrez le fichier.   

Relancez votre application streamlit si nécessaire:  

```
streamlit run slt_linechart_app.py
```

Vérifiez le résultat qui s'affiche sur votre navigateur.  

Retournez sur le terminal et exécuter les commandes suivantes:

```
git status
git add slt_linechart_app.py
git commit -m 'ajout d'un line chart'
git push origin linechart
```
* Fusionner la nouvelle fonctionnalité avec la branch **main**.  

```
git checkout main
git merge linechart
```

### Streamlit bar Chart:

Une application simple pour afficher un graphique en barre:

```
git branch barchart     # Créer une nouvelle branch

git branch            # vérifier que la nouvelle branch existe

git checkout barchart   # se positionner sur la nouvelle branch
```

Créez un nouveau fichier slt_barchart_app.py Copiez les lignes de code suivantes dans votre fichier slt_barchart_app.py:  

```
import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
 
st.header("Bar Chart")
 
data = {"a":[23, 12, 78, 4, 54], "b":[0, 13 ,88, 1, 3], 
"c":[45, 2, 546, 67, 56]}
 
df = pd.DataFrame(data)
df
st.bar_chart(data=df)

```

Enregistrez le fichier.   

Relancez votre application streamlit si nécessaire:  

```
streamlit run slt_barchart_app.py
```

Vérifiez le résultat qui s'affiche sur votre navigateur.  

Retournez sur le terminal et exécuter les commandes suivantes:

```
git status
git add slt_barchart_app.py
git commit -m 'ajout d'un bar chart'
git push origin barchart
```
* Fusionner la nouvelle fonctionnalité avec la branch **main**.  

```
git checkout main
git merge barchart
```


### Streamlit Maps:

Une application simple pour afficher un graphique en Maps:

```
git branch maps     # Créer une nouvelle branch

git branch            # vérifier que la nouvelle branch existe

git checkout maps   # se positionner sur la nouvelle branch
```

Créez un nouveau fichier slt_maps_app.py Copiez les lignes de code suivantes dans votre fichier slt_mpas_app.py:  

```
import streamlit as st
import pandas as pd
import numpy as np

st.header("Map")
 
data = {"lat":[28.704060, 28.459497, 13.082680, 17.385044, 23.0225],
        "lon":[77.102493, 77.026634, 80.270721, 78.486671, 72.5714],
        "City": ["Delhi", "Gurgaon", "Chennai", "Hyderabad", "Ahemdabad"]}
 
df = pd.DataFrame(data)
df
st.map(data=df)

```

Enregistrez le fichier.   

Relancez votre application streamlit si nécessaire:  

```
streamlit run slt_maps_app.py
```

Vérifiez le résultat qui s'affiche sur votre navigateur.  

Retournez sur le terminal et exécuter les commandes suivantes:

```
git status
git add slt_maps_app.py
git commit -m 'ajout d'une map'
git push origin maps
```
* Fusionner la nouvelle fonctionnalité avec la branch **main**.  

```
git checkout main
git merge maps
```