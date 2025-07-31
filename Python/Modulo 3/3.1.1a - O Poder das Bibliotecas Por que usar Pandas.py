import csv

# Lista para guardar apenas os valores de temperatura
temperaturas = []

with open('dados_rio.csv', mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)

    # Pula a primeira linha (o cabeçalho)
    next(leitor_csv)

    # Itera sobre as linhas para extrair a temperatura
    for linha in leitor_csv:
        # A temperatura está na 4ª coluna (índice 3)
        temperatura_str = linha[3]
        temperaturas.append(float(temperatura_str))

# Agora, calculamos a média manualmente
media = sum(temperaturas) / len(temperaturas)

print(f"A temperatura média da água é: {media:.2f}°C")