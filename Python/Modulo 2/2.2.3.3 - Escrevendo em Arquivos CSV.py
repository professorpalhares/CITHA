import csv

# Nossos dados: a primeira lista é o cabeçalho
dados_peixes = [
    ['nome_popular', 'nome_cientifico', 'risco_extincao'],
    ['Pirarucu', 'Arapaima gigas', 'Vulneravel'],
    ['Tambaqui', 'Colossoma macropomum', 'Quase Ameacado'],
    ['Tucunare', 'Cichla ocellaris', 'Pouco Preocupante']
]

nome_arquivo = 'peixes_catalogados.csv'

# Abrimos o arquivo em modo de escrita ('w')
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    # .writerows() escreve todas as listas de uma vez
    escritor_csv.writerows(dados_peixes)

print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")