# 🏠 SalesHouses – Simulateur Intelligent d’Évaluation Immobilière

## 📌 Contexte du Projet

Ce projet a été développé dans le cadre de mon rôle de développeur IA junior au sein de l’entreprise **SalesHouses**, une plateforme marocaine spécialisée dans les transactions immobilières (achat/vente).

L’objectif est de concevoir un **simulateur intelligent** capable d’estimer le **prix de vente d’un appartement** à partir de ses caractéristiques. L’outil cible le **marché immobilier marocain** et permet à l’utilisateur d’obtenir une prédiction précise en renseignant les informations clés du bien.

---

## 🧠 Objectif Technique

Mettre en place un **modèle de régression supervisée** permettant de prédire le prix d’un bien immobilier à partir d’un jeu de données historiques. Le projet comprend plusieurs étapes : analyse des données, préparation, entraînement de modèles, évaluation, et livraison d’un modèle final exploitable dans une application web.

---

## 📁 Structure du projet
├── SALESHOUSES
│ ├── sales.ipynb
│ ├── appartements-data.csv
│ ├── .env
│ └── model.pkl



## 🔍 Étapes Réalisées

### 📥 Chargement des données
- Importation via `pandas`
- Exploration initiale avec `df.head()`, `df.info()`, etc.

### 📊 Analyse exploratoire des données (EDA)
- Analyse des types, dimensions, valeurs manquantes et doublons
- Visualisation des distributions et des corrélations

### 🧹 Prétraitement des données
- **Nettoyage :**
  - Conversion de la colonne `price` en `float`
  - Suppression de colonnes inutiles comme `equipment` et `link`
- **Extraction des équipements :**
  - Utilisation de `str.get_dummies()` pour créer des colonnes booléennes
- **Traitement des villes :**
  - Standardisation des noms de ville (arabe → français)
  - Valeurs manquantes remplacées par `"Unknown"`
- **Imputation des valeurs manquantes :**
  - Médiane pour les colonnes numériques
  - `"Unknown"` pour les catégorielles
- **Détection des outliers :**
  - Utilisation de Z-score, IQR, boîtes à moustaches
  - Suppression des lignes anormales (ex: `price`, `surface_area`)
- **Encodage des variables catégorielles :**
  - `LabelEncoder` sur `city_name`
- **Mise à l’échelle :**
  - `MinMaxScaler` ou `StandardScaler` sur les colonnes numériques

### 🎯 Sélection des variables explicatives
- Variables numériques avec corrélation > 0.15
- Vérification de la multicolinéarité


## 🤖 Modélisation

### Modèles testés :
- Régression Linéaire
- Random Forest Regressor
- SVR (Support Vector Regressor)
- Gradient Boosting Regressor

### Évaluation :
- **Métriques utilisées :**
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - RMSE (Root Mean Squared Error)
  - R² Score

- **Validation croisée :**
  - `cross_val_score` avec k=5

- **Optimisation :**
  - `GridSearchCV` / `RandomizedSearchCV` pour les hyperparamètres



