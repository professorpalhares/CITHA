import pandas as pd

dados = {
    'local': ['Encontro das Águas', 'Frente a Manaus', 'Lago Janauari', 'Parintins', 'Frente a Manaus', 'Lago Janauari', 'Encontro das Águas'],
    'especie': ['Tambaqui', 'Tucunaré', 'Pirarucu', 'Tambaqui', 'Jaraqui', 'Tucunaré', 'Pirarucu'],
    'quantidade': [45.0, 22.0, 10.0, 56.0, 89.0, 15.0, None],
    'ph_agua': [6.8, 6.5, 7.1, None, 6.6, 7.0, 6.9]
}
df_peixes = pd.DataFrame(dados)

# Selecionando a coluna 'especie'
coluna_especies = df_peixes['especie']

print("--- Conteúdo da Coluna 'especie' ---")
print(coluna_especies)

print("\nTipo do objeto retornado:")
print(type(coluna_especies))