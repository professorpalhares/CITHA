import os

# Nome da pasta e do arquivo que queremos
pasta_dados = "dados"
arquivo_relatorio = "relatorio_final.csv"

# Construindo o caminho de forma segura
caminho_completo = os.path.join(pasta_dados, arquivo_relatorio)

print(f"O caminho construído é: {caminho_completo}")

# Você pode juntar vários componentes
caminho_mais_longo = os.path.join("ProjetoCITHA", "dados", "sensores", "log.txt")
print(f"Caminho mais complexo: {caminho_mais_longo}")