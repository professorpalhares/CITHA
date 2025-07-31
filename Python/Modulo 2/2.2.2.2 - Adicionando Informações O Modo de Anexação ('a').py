# Lista de novas observacoes
novas_observacoes = [
    "Observado um bando de araras-canga (Ara macao).",
    "Rastros de onca-pintada (Panthera onca) perto do igarape.",
    "Ninho de uirapuru-verdadeiro (Cyphorhinus arada) encontrado.",
    "Fui picado..."
]

# Abrindo o arquivo em modo de anexacao ('a')
with open("diario_fauna.txt", 'a') as diario:
    # Adicionando um separador para organizar
    diario.write("\n--- Novas Observacoes ---\n")
    # Percorrendo a lista e escrevendo cada nova observacao
    for obs in novas_observacoes:
        diario.write(obs + "\n")

print("Diario de campo atualizado!")