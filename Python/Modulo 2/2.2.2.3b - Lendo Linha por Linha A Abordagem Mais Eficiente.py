print("Analisando temperaturas em busca de alertas:")
with open("temperaturas.txt", 'r') as f:
    for linha in f:
        # .strip() remove espacos em branco e novas linhas ('\n')
        temperatura_str = linha.strip()

        # Convertemos a string para um numero float
        temperatura_float = float(temperatura_str)

        if temperatura_float > 35.0:
            print(f"ALERTA: Temperatura elevada detectada! -> {temperatura_float} C")