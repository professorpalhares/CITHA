# Lendo o conteudo completo do nosso diario
with open("diario_fauna.txt", 'r') as diario:
    conteudo_completo = diario.read()

print("--- Conteudo completo do Diario ---")
print(conteudo_completo)