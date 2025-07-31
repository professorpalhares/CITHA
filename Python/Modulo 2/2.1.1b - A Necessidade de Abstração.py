def verificar_sensor(nome_sensor, valor, unidade, min_aceitavel, max_aceitavel):
    """
    Verifica o dado de um sensor e imprime seu status.
    """
    print(f"Lendo dado de {nome_sensor}: {valor}{unidade}")
    if not (min_aceitavel <= valor <= max_aceitavel):
        print(f"ALERTA: {nome_sensor} fora do padrao!")
    else:
        print(f"{nome_sensor} OK.")
    print("-" * 20)

# Agora, usamos nossa funcao para cada sensor
verificar_sensor("Umidade do solo", 45.7, "%", 30, 70)
verificar_sensor("Temperatura do ar", 31.5, " C", 22, 30)
verificar_sensor("pH da agua", 5.8, "", 6.5, 8.5)