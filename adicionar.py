import json
arquivo = 'estoque.json'

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

def adicionarProduto():
    idproduto = int(input("Informe o ID do produto: "))
    nome = input("Informe o nome do produto: ")
    while not nome.isalpha():
        print("Adicione apenas letras.")
        nome = input("Informe o nome do produto: ")
    quantidade_input = input("Informe a quantidade que tem do produto: ")
    while not quantidade_input.isdigit():
        print("Adicione apenas números.")
        quantidade_input = input("Informe a quantidade que tem do produto: ")
    quantidade = int(quantidade_input)
    categoria = input("Informe a categoria do produto: ")
    while not categoria.isalpha():
        print("Adicione apenas letras.")
        categoria = input("Informe a categoria do produto: ")
    dataEntrada = input("Informe a data de entrada do produto (DD/MM/AAAA): ")
        
    item = {
        "idproduto": idproduto,
        "nome": nome,
        "quantidade": quantidade,
        "categoria": categoria,
        "dataEntrada": dataEntrada
            }
    dados.append(item)
        
    with open("estoque.json","w", encoding="utf-8") as adicionar:
        json.dump(dados, adicionar, indent=4, ensure_ascii=False)

    print("Produto salvo com sucesso!")