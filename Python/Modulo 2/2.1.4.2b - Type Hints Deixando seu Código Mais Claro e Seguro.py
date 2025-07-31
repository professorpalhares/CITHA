# Importamos os tipos que precisamos do módulo typing
from typing import List, Dict, Optional

def encontrar_sensor_com_maior_valor(leituras: List[Dict[str, float]]) -> Optional[str]:
    """Analisa uma lista de leituras de sensores e encontra o sensor com maior valor.

    Args:
        leituras: Uma lista onde cada item é um dicionário.
                  Cada dicionário deve ter uma chave 'sensor' (str) e 'valor' (float).

    Returns:
        O nome (str) do sensor que registrou o maior valor.
        Retorna None se a lista de leituras estiver vazia.
    """
    if not leituras:
        return None  # Retorna None para indicar que nenhum sensor foi encontrado

    maior_leitura = -1.0
    sensor_destaque = ""

    for leitura in leituras:
        # Usamos .get() para acessar as chaves de forma segura
        nome_sensor = leitura.get('sensor', 'Desconhecido')
        valor = leitura.get('valor', -1.0)

        if valor > maior_leitura:
            maior_leitura = valor
            sensor_destaque = nome_sensor

    return sensor_destaque

# Dados coletados de um igarapé
dados_sensores = [
    {'sensor': 'pH', 'valor': 6.8},
    {'sensor': 'Turbidez', 'valor': 4.5},
    {'sensor': 'Oxigênio Dissolvido', 'valor': 7.2}
]

sensor_alerta = encontrar_sensor_com_maior_valor(dados_sensores)
print(f"Sensor com maior leitura: {sensor_alerta}")

# Testando com uma lista vazia
sensor_vazio = encontrar_sensor_com_maior_valor([])
print(f"Resultado para lista vazia: {sensor_vazio}")