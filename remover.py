import json
arquivo = 'estoque.json'

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

def removerProduto():

    idproduto = int(input("Informe o ID do produto para removê-lo: "))
    encontrado = False

    for item in dados:
        if item['idproduto'] == idproduto:
            dados.remove(item)
            encontrado = True
            print("Produto removido com sucesso!")
            break

    if not encontrado:
        print("Produto não encontrado.")
    else:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("Alterações salvas no arquivo.")