import json
arquivo = 'estoque.json'

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

def buscarItemPorNome():
    
    nome = input("Informe o nome do produto que deseja buscar: ")
    encontrado = False

    for item in dados:
        if nome.lower() in item['nome'].lower():
            print(item)
            encontrado = True

    if not encontrado:
        print("Produto não encontrado.")