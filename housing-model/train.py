import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
import mlflow
import mlflow.sklearn
import mlflow.models.signature

# Charger le dataset
df = pd.read_csv("housing.csv")

# Supprimer la colonne non numérique
df_numeric = df.drop("ocean_proximity", axis=1)

# Supprimer les lignes contenant des NaN
df_numeric = df_numeric.dropna()

# Préparer les données
features = df_numeric.drop("median_house_value", axis=1)
target = df_numeric["median_house_value"]

# Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Entraînement du modèle avec régression Lasso
alpha_value = 1.0  # Valeur de régularisation, ajustable selon besoin
model = Lasso(alpha=alpha_value)
model.fit(X_train, y_train)

# Évaluation du modèle
score = model.score(X_test, y_test)
print("Score du modèle :", score)

# Inférer la signature du modèle à partir des données d'entraînement
signature = mlflow.models.signature.infer_signature(X_train, model.predict(X_train))

# Journalisation avec MLflow
mlflow.set_experiment("Housing Model")
with mlflow.start_run() as run:
    mlflow.log_param("model", "Lasso")
    mlflow.log_param("alpha", alpha_value)
    mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(
        model,
        "model",
        input_example=X_train.head(1),
        signature=signature
    )
    
    # Enregistrement dans le registre de modèles
    run_id = run.info.run_id
    print(run_id)
    model_uri = f"runs:/{run_id}/model"
    registered_model = mlflow.register_model(model_uri, "HousingLassoModel")
    print("Modèle enregistré dans le registre, version :", registered_model.version)