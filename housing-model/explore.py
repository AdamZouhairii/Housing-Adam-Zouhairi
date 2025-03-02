import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lis le fichier CSV contenant les données de logement
df = pd.read_csv("housing.csv")

# Affiche les statistiques descriptives du DataFrame
print(df.describe())

# Crée une matrice de graphiques en paires pour visualiser les relations entre les variables
sns.pairplot(df)

# Affiche les graphiques
plt.show()