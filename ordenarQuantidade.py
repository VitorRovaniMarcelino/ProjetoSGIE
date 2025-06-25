import json
arquivo = 'estoque.json'

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

def ordenarQuantidade():
    dados.sort(key=lambda x: x['quantidade'], reverse=True)
    print("\nProdutos ordenados por quantidade:\n")
    for item in dados:
        print(item)