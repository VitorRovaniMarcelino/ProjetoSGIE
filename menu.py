import json

arquivo = 'estoque.json'

with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

while True:
    print(20*"=", "MENU DE GERENCIAMENTO INVENTÁRIO",20*"=")
    print("1 - Adicionar Item") 
    print("2 - Remover Item")
    print("3 - Atualizar Item")
    print("4 - Buscar item por nome")
    print("5 - Ordenar por categoria")
    print("6 - Ordenar por quantidade")
    print("7 - Ordenar por data de entrada")
    print("0 - Sair")

    opcao = int(input("Faça a sua escolha: "))
    match opcao:
        case 1:
                idproduto = int(input("Informe o id do produto: "))
                nome = input("Informe o nome do produto: ")
                quantidade = int(input("Informe a quantidade que tem do produto: "))
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
                
        case 2:
                idproduto = int(input("Informe o id do produto para remove-lo: "))
                encontrado = False

                for item in dados:
                    if item['idproduto'] == idproduto:
                        dados.remove(item)
                        encontrado = True
                        print("Produto removido com sucesso!")
                        break

                if not encontrado:
                    print("Produto não encontrado.")

                with open("estoque.json", "w", encoding="utf-8") as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)

                print("Alterações salvas no arquivo.")
        
        case 3:
                print("Função de atualizar ainda não implementada.")
