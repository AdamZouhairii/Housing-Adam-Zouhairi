import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")
print(df.describe())
sns.pairplot(df)
plt.show()