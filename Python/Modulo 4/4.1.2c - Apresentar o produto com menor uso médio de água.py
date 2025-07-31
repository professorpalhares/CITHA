import pandas as pd

df = pd.read_csv("dados_agricolas.csv")

# Passo 4: Apresentar o produto com menor uso médio de água
print("\n--- 4. Cultivo com Menor Uso Médio de Água ---")
uso_agua_medio = df.groupby('tipo_cultivo')['uso_agua'].mean().reset_index()
cultivo_menor_uso_agua = uso_agua_medio.loc[uso_agua_medio['uso_agua'].idxmin()]
print(cultivo_menor_uso_agua)