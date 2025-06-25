import json
arquivo = 'estoque.json'

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

def ordenarCategoria():
    dados.sort(key=lambda itens: itens['categoria'].lower())
    print("\nProdutos ordenados por categoria:\n")
    for item in dados:
        print(item)