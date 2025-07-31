import json

nome_arquivo = 'sensor_igarap_v1.json'

print(f"--- Lendo dados do sensor do arquivo: {nome_arquivo} ---")

with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_json:
  # json.load() lê o arquivo e converte o JSON para um objeto Python
  dados_sensor = json.load(arquivo_json)

# Agora 'dados_sensor' é um dicionário Python comum!
local = dados_sensor['local']
id_sensor = dados_sensor['id_sensor']
print(f"Local do Sensor: {local} (ID: {id_sensor})")

print("\nÚltimas Leituras Registradas:")
# Podemos iterar sobre a lista de leituras
for leitura in dados_sensor['leituras']:
  param = leitura['parametro']
  val = leitura['valor']
  unid = leitura['unidade']
  print(f" -> {param}: {val} {unid}")