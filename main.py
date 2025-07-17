
import pandas as pd

#** Partie 1: Chargement des données
#1-Importer les données à l’aide de pandas
df = pd.read_csv('appartements-data.csv')

#2-Vérifier le type et la structure des colonnes (df.info() et df.head()).
print(df.info()) #permet de donne les collone exixst et aussi le type de chaque collone
print(df.head()) #permet de donner les 5 premier ligne de tableau

#** Partie 2: Analyse exploratoire des données (EDA)
#1-Comprendre la structure générale du jeu de données (types, dimensions, aperçus).

#type deux méthodes :
print(df.dtypes)
print(df['salon'].dtypes)

#pour les dimention de data
print(df.shape)

#pour apercus just les nom des columns 
print(df.columns)

#Identifier les valeurs manquantes et les doublons.


# Détection et suppression des valeurs aberrantes
# Utiliser des méthodes statistiques (boîtes à moustaches, z-score, IQR) pour détecter les outliers

# Visualisation des outliers

# Traitement des outliers



####################################""
