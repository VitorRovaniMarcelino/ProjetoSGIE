import json
arquivo = 'estoque.json'

def atualizarProduto():
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)
    idproduto = int(input("Informe o ID do produto que deseja atualizar: "))
    encontrado = False

    for item in dados:
        if item['idproduto'] == idproduto:
            print("Produto encontrado!\nInforme os novos dados:\n")
            item['idproduto'] = int(input("Novo ID do produto: "))
            item['nome'] = input("Novo nome do produto: ")
            item['quantidade'] = int(input("Nova quantidade do produto: "))
            item['categoria'] = input("Nova categoria do produto: ")
            item['dataEntrada'] = input("Nova data de entrada do produto (DD/MM/AAAA): ")
            encontrado = True
            print("Produto atualizado com sucesso!")
            break

    if encontrado:
        with open("estoque.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("Alterações salvas no arquivo.")
    else:
        print("Produto não encontrado.")

                