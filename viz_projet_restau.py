import glob
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from collections import Counter
from collections import OrderedDict
import plotly.express as px
from wordcloud import WordCloud



###### CODE CMD
#cd.ipython
#streamlit run viz_projet_perso.py




## Nettoyage / Analyses - documentation

## chargement de la base
path_file = os.path.join("c:\\", 'Users', 'celin','.ipython','PROJET PERSO','restaurant_data_kaggles.csv')
path_file= os.path.normpath(path_file)
df=pd.read_csv("restaurant_data_kaggles.csv", sep = ',')

# renomer les colonnes
df_resto_lyon = df.rename(columns={'restaurant_name ' : 'nom_restaurant', 'review_number ':'nombre_d_avis', ' food_type ':'type_nourriture', ' ranking ':'classement',' overallRating  ':'note', ' wifi ':'wifi', ' livraison ':'livraison', ' average_price ':'prix_moyen', ' lat ':'latitude', ' lng ':'longitude', ' district ':'arrondissement'})

# remplacer les données categorielles manuscrites en chiffres pour faciliter l'analyse
# yes = 1, no =0

df_resto_lyon.loc[df_resto_lyon.livraison == 'no','livraison'] = 0
df_resto_lyon.loc[df_resto_lyon.livraison == 'yes','livraison'] = 1

df_resto_lyon.loc[df_resto_lyon.wifi == 'no','wifi'] = 0
df_resto_lyon.loc[df_resto_lyon.wifi == 'yes','wifi'] = 1

df_resto_lyon.loc[df_resto_lyon.latitude == 'no information','latitude'] = 0
df_resto_lyon.loc[df_resto_lyon.longitude == 'no information','longitude'] = 0


df_resto_lyon = df_resto_lyon.replace(r'^\s*$', np.nan, regex=True)

def test_float(v):
    try:
        float(v)
        return True
    except ValueError:
        return False
df_resto_lyon.latitude.apply(test_float)

datrating_low = df_resto_lyon.loc[df_resto_lyon['note'] != 'no information']
datrating_low = datrating_low.loc[datrating_low['note'] < str(2.0)]
prix_low = df_resto_lyon.loc[df_resto_lyon['prix_moyen'] != 'no information']
prix_low = df_resto_lyon.loc[df_resto_lyon['prix_moyen'] != 'no informations']
prix_low = datrating_low.loc[datrating_low['prix_moyen'] != object]

data = df_resto_lyon['type_nourriture'].str.replace("|","")
data = df_resto_lyon['note'].str.replace("|","")

datrating = df_resto_lyon.loc[df_resto_lyon['note'] != 'no information']
datrating['note'] = datrating.note.astype(float)
datrating = datrating.loc[datrating['note'] > 4.5]

# top 5 des arrondissements lyonnais où il y a le plus de restaurants

k=0
arr=[]
while k<len(df_resto_lyon['arrondissement']):
    arr+=Counter(df_resto_lyon['arrondissement'][k].split()).most_common()
    k+=1
subclass_arr = [j for j in arr if j[0] != 'Lyon' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Villeurbanne' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Saint-Priest' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'en' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Vaulx' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Velin' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Bron' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Chaponnay' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Decines-Charpieu' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Charbonni\xc3\xa8res-les-Bains' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Limonest' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Chassieu' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Ecully' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Francheville' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'LYON' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'lyon' ]
subclass_arr = [j for j in subclass_arr if j[0] != 'Charbonnières-les-Bains  ' ]

val_arr=  OrderedDict(sorted(Counter(subclass_arr).most_common(5), key=lambda t: t[1],reverse=False)).values()
keys_arr=  OrderedDict(sorted(Counter(subclass_arr).most_common(5), key=lambda t: t[1],reverse=False)).keys()
keys_list = [x[0] for x in keys_arr]

# top des restaurants
k1=0
arr1=[]
while k1<len(df_resto_lyon['arrondissement']):
    arr1+=Counter(df_resto_lyon['arrondissement'][k1].split()).most_common()
    k1+=1
subclass_arr1 = [j for j in arr if j[0] != 'Lyon' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Villeurbanne' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Saint-Priest' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'en' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Vaulx' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Velin' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Bron' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Chaponnay' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Decines-Charpieu' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Charbonni\xc3\xa8res-les-Bains' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Limonest' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Chassieu' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Ecully' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Francheville' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'LYON' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'lyon' ]
subclass_arr1 = [j for j in subclass_arr if j[0] != 'Charbonnières-les-Bains  ' ]

# les types de nourriture

data = df_resto_lyon['type_nourriture'].str.replace("|","")
i=0
# fonction split permet de recuperer pour chaque ligne les mots separés (
# on stock ces mots dans un tableau que l'on nomme u 
u=[]
while i<len(data):
    u+=Counter(data[i].split()).most_common()
    i+=1
    
# supprime les mots inutiles ou repetitifs de la liste u pour une meilleure analyse
subclass = [j for j in u if j[0] != 'no' ]
subclass = [j for j in subclass if j[0] != 'de' ]
subclass = [j for j in subclass if j[0] != 'à' ]
subclass = [j for j in subclass if j[0] != 'bienvenus' ]
subclass = [j for j in subclass if j[0] != 'restauration' ]
subclass = [j for j in subclass if j[0] != 'Restauration' ]
subclass = [j for j in subclass if j[0] != '&' ]
subclass = [j for j in subclass if j[0] != 'food' ]
subclass = [j for j in subclass if j[0] != 'cuisine' ]
subclass = [j for j in subclass if j[0] != 'rue' ]
subclass = [j for j in subclass if j[0] != 'choix' ]
subclass = [j for j in subclass if j[0] != 'plats' ]
subclass = [j for j in subclass if j[0] != 'gluten' ]
subclass = [j for j in subclass if j[0] != 'sans' ]
subclass = [j for j in subclass if j[0] != 'Saine' ]
subclass = [j for j in subclass if j[0] != 'information' ]

val_arr1=  OrderedDict(sorted(Counter(subclass_arr1).most_common(10), key=lambda t: t[1],reverse=True)).values()
keys_arr1=  OrderedDict(sorted(Counter(subclass_arr1).most_common(10), key=lambda t: t[1],reverse=True)).keys()
keys_list1 = [x[0] for x in keys_arr1]

height = OrderedDict(sorted(Counter(subclass).most_common(15), key=lambda t: t[1],reverse=True)).values()
bars = OrderedDict(sorted(Counter(subclass).most_common(15), key=lambda t: t[1],reverse=True)).keys()
y_pos = np.arange(len(bars))


# Titre / intro
# toute la largeur de la page
st. set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'> Dans quel restaurant je mange à Lyon ? </h1>", unsafe_allow_html=True)

st.subheader("Objectif :")
st.subheader("Analyser des données extraites du site Kaggle (enquête TripAdvisor), de 2021, dans le but de connaitre les meilleurs restaurants Lyonnais.")
st.subheader("Le jeu de données couvre plus de 3000 informations sur les restaurants Lyonnais.")



## Visualisation
# 1er graphique : les arrondissements où l'on trouve le plus de restaurants

st.subheader('1. Quel type de nourriture mange-t-on ?')
fig, ax = plt.subplots(figsize=(20,4))
ax = plt.subplot()
my_colors = ['red','orange','#ffe119','#ff6666','#42d4f4','blue','#f032e6','#e6beff','#911eb4','#3cb44b', '#ffcc99', '#99ff99', '#66b3ff']
plt.barh(y_pos, list(height), color=my_colors)
plt.yticks(y_pos, bars)
plt.title('Les types de nourriture les plus appréciés')
plt.show()
st.pyplot(fig)

# 2e graphique / Les meilleurs restaurants

st.subheader('2. Où trouver The restaurant ?')
fig, ax = plt.subplots(figsize=(50,50))
fig=px.histogram(x=list(keys_list), y= list(val_arr),text_auto=True, color=list(val_arr))
ax=fig.update_layout(yaxis_title_text='Nombre de restaurants', xaxis_title_text='Arrondissements')
ax=fig.update_layout(showlegend=False)
st.plotly_chart(fig)    
    
# graphique 3 : le type de nourriture
col1, col2 = st.columns(2)
with col1:
    st.subheader('3. The place to be ?')
    restau = ['le Neuvième Art', 'Aromatic', 'Konnichiwa','Mini Cocina', 'BT AVONE','Delta 2', 'Au petit Vatel', 'Le Jardin du Paradis', 'Mas Amor Por Favor', 'Garden']
    frequencies = [1,1,1,1,1,1,1,1,1,1]
    text = ''
    for i, word in enumerate(restau):
        text = text + frequencies[i] * (word + ',') 
    d = dict(zip(restau, frequencies))
    fig, ax = plt.subplots(figsize=(10,10))
    wordcloud = WordCloud(collocations=False,colormap= 'rainbow',width=300,background_color = 'white', height=200,max_font_size=100, prefer_horizontal = 0.9, min_font_size=4).generate_from_frequencies(d)
    wordcloud=ax.imshow(wordcloud, interpolation = 'bilinear')
    wordcloud=plt.axis("off")
    wordcloud=plt.margins(x=0, y=0)
    wordcloud=plt.show()
    st.pyplot(fig)
with col2 :
    st.write("")
    
st.subheader("Pour conclure")
st.subheader("Les répondants au questionnaire ont préféré la cuisine : Française, Européenne et végétarienne.")
st.subheader("on voit sur le 2e graphique que les restaurants sont concentrés sur les 2e, 3e et 6e arrondissements.")
st.subheader("Le top 3 des restaurants préférés des Lyonnais est : le Neuvième Art, Aromatic et Konnichiwa.")
st.subheader("Le graphique utilisé s'appelle un Worlcloud, et oui c'est un graphique !")