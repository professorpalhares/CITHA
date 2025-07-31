import csv

nome_arquivo = 'qualidade_agua.csv'

print("Analisando niveis de turbidez...\n")
with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
    # Criamos um leitor que transforma cada linha em um dicionario
    leitor_dict = csv.DictReader(arquivo_csv)

    for linha in leitor_dict:
        # Acessamos os dados pela chave (nome da coluna)
        local = linha['local']
        turbidez = float(linha['turbidez']) # Nao esqueca de converter para numero!

        if turbidez > 5.0:
            print(f"ALERTA: Turbidez elevada em '{local}'. Valor: {turbidez}")