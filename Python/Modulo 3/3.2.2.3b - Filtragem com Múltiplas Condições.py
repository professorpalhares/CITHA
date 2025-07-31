import pandas as pd

dados = {
    'local': ['Encontro das Águas', 'Frente a Manaus', 'Lago Janauari', 'Parintins', 'Frente a Manaus', 'Lago Janauari', 'Encontro das Águas'],
    'especie': ['Tambaqui', 'Tucunaré', 'Pirarucu', 'Tambaqui', 'Jaraqui', 'Tucunaré', 'Pirarucu'],
    'quantidade': [45.0, 22.0, 10.0, 56.0, 89.0, 15.0, None],
    'ph_agua': [6.8, 6.5, 7.1, None, 6.6, 7.0, 6.9]
}
df_peixes = pd.DataFrame(dados)

# Criando as duas máscaras separadamente
mascara_ph_acido = df_peixes['ph_agua'] < 6.7
mascara_pirarucu = df_peixes['especie'] == 'Pirarucu'

# Combinando as máscaras com o operador OU (|)
registros_importantes = df_peixes[mascara_ph_acido | mascara_pirarucu]

print("--- Registros com pH ácido OU da espécie Pirarucu ---")
print(registros_importantes)