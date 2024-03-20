import json
import csv

# Função para converter JSON para CSV
def convert_json_to_csv(json_file, csv_file):
    # Abre o arquivo JSON e carrega os dados
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Abre o arquivo CSV para escrita
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Cria um objeto escritor CSV
        csvwriter = csv.writer(csvfile)
        
        # Escreve a linha do cabeçalho
        csvwriter.writerow(json_data[0].keys())
        
        # Escreve as linhas de dados
        for row in json_data:
            csvwriter.writerow(row.values())

# Chama a função para converter 'data.json' para 'data.csv'
convert_json_to_csv('data.json', 'data.csv')
