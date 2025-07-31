import pandas as pd

dados = {
    'local': ['Encontro das Águas', 'Frente a Manaus', 'Lago Janauari', 'Parintins', 'Frente a Manaus', 'Lago Janauari', 'Encontro das Águas'],
    'especie': ['Tambaqui', 'Tucunaré', 'Pirarucu', 'Tambaqui', 'Jaraqui', 'Tucunaré', 'Pirarucu'],
    'quantidade': [45.0, 22.0, 10.0, 56.0, 89.0, 15.0, None],
    'ph_agua': [6.8, 6.5, 7.1, None, 6.6, 7.0, 6.9]
}
df_peixes = pd.DataFrame(dados)

# Passo 1: Criar a máscara booleana
# Isso cria uma Series de True/False
mascara_alta_quantidade = df_peixes['quantidade'] > 50
print("--- Máscara Booleana (Quantidade > 50) ---")
print(mascara_alta_quantidade)

# Passo 2: Aplicar a máscara ao DataFrame
coletas_grandes = df_peixes[mascara_alta_quantidade]
print("\n--- Coletas com mais de 50 indivíduos ---")
print(coletas_grandes)