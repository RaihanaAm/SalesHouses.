
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
# avec Minscaller
#       price  salon  nb_rooms  nb_baths  surface_area
# 0  0.900899    0.0  0.333333  0.666667      0.458904
# 1  0.538281    0.0  0.333333  0.666667      0.541096
# 2  0.608102    0.0  0.333333  0.666667      0.424658
# 3  0.405396    0.0  0.000000  0.333333      0.253425
# 4  0.342332    0.0  0.666667  1.000000      0.541096
# 5  0.355846    0.0  0.666667  0.666667      0.369863
# 6  0.351341    0.0  0.333333  0.333333      0.363014
# 7  0.896395    0.0  0.333333  0.666667      0.458904
# 8  0.340080    0.0  0.333333  0.666667      0.390411
# 9  0.355846    0.0  0.666667  0.666667      0.589041
# avec standael
#       price  salon  nb_rooms  nb_baths  surface_area
# 0  2.448826    0.0 -0.452470  0.598316     -0.099952
# 1  0.653713    0.0 -0.452470  0.598316      0.360732
# 2  0.999356    0.0 -0.452470  0.598316     -0.291903
# 3 -0.004124    0.0 -2.205253 -1.245358     -1.251662
# 4 -0.316318    0.0  1.300313  2.441989      0.360732
# 5 -0.249419    0.0  1.300313  0.598316     -0.599026
# 6 -0.271719    0.0 -0.452470 -1.245358     -0.637417
# 7  2.426527    0.0 -0.452470  0.598316     -0.099952
# 8 -0.327468    0.0 -0.452470  0.598316     -0.483855
# 9 -0.249419    0.0  1.300313  0.598316      0.629465