import csv

nome_arquivo = 'qualidade_agua.csv'

print(f"Lendo dados do arquivo: {nome_arquivo}\n")
# O argumento newline='' é importante para evitar linhas em branco inesperadas
with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
    # Criamos um objeto leitor
    leitor_csv = csv.reader(arquivo_csv)

    # Iteramos sobre cada linha do leitor
    for linha in leitor_csv:
        print(linha)