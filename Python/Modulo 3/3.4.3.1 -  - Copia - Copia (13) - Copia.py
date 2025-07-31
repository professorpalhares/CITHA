import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Para garantir que nossos exemplos sejam reprodutíveis, vamos criar os dados
np.random.seed(42) # Semente para reprodutibilidade
dados = {
    'id_arvore': range(1, 101),
    'regiao': np.random.choice(['Reserva Tapajós', 'Floresta Jari'], 100),
    'diametro_cm': np.random.normal(loc=120, scale=25, size=100),
    'producao_kg': np.nan # Vamos preencher com base no diâmetro
}
df_safra = pd.DataFrame(dados)

# Criando uma relação realista entre diâmetro e produção com um pouco de ruído
df_safra['producao_kg'] = (df_safra['diametro_cm'] * 0.45) + np.random.normal(loc=0, scale=10, size=100)
# Garantindo que não haja produção negativa
df_safra['producao_kg'] = df_safra['producao_kg'].clip(lower=5)

print("--- Primeiras 5 linhas do nosso conjunto de dados ---")
print(df_safra.head())

print("\n--- Informações gerais do DataFrame ---")
df_safra.info()