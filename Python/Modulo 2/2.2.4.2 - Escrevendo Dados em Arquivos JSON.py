import json

nova_ficha = {
  "id_especie": "FLR-001",
  "nome_popular": "Vitória-Régia",
  "nome_cientifico": "Victoria amazonica",
  "familia": "Nymphaeaceae",
  "coletor": "A. Silva",
  "locais_avistados": [
    {"local": "Lago Janauari", "coords": [-3.456, -60.123]},
    {"local": "Rio Solimões", "coords": [-3.123, -59.456]}
  ]
}

nome_arquivo = 'ficha_especie_001.json'

with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo_json:
  # json.dump() escreve o objeto Python no arquivo em formato JSON
  # 'indent=4' formata o arquivo de forma legível para humanos
  json.dump(nova_ficha, arquivo_json, indent=4, ensure_ascii=False)

print(f"Ficha da espécie salva com sucesso no arquivo '{nome_arquivo}'!")