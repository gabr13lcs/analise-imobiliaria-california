from sklearn.datasets import fetch_california_housing
import pandas as pd

# Carrega o dataset
housing = fetch_california_housing()

# Monta o DataFrame
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['preco'] = housing.target

# Exporta para CSV
df.to_csv("california_housing.csv", index=False)

print(f"Dataset exportado com sucesso! {len(df)} registros.")
