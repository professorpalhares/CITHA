# O nome do arquivo que queremos criar
nome_arquivo = "log_estacao_1.txt"

# Usamos 'with open' para abrir o arquivo em modo de escrita ('w')
# A variável 'arquivo' nos dá acesso para interagir com o arquivo
with open(nome_arquivo, 'w') as arquivo:
    # O método .write() escreve uma string no arquivo
    arquivo.write("Registro de operacoes da Estacao de Monitoramento Alpha.\n")
    arquivo.write("Dados coletados a partir de 24/07/2025.")

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")