from adicionar import *
from remover import *
from atualizar import *
from buscaritem import *
from ordenarcategoria import *
from ordenarQuantidade import *

while True:
    print(20*"=", "MENU DE GERENCIAMENTO INVENTÁRIO",20*"=")
    print("1 - Adicionar Item") 
    print("2 - Remover Item")
    print("3 - Atualizar Item")
    print("4 - Buscar item por nome")
    print("5 - Ordenar por categoria")
    print("6 - Ordenar por quantidade")
    print("0 - Sair")

    opcao = int(input("Faça a sua escolha: "))
    match opcao:
        case 1:
                adicionarProduto()
                
        case 2:
                removerProduto()
                
        case 3:
                atualizarProduto()
            
        case 4:
                buscarItemPorNome()

        case 5:
                ordenarCategoria()

        case 6:
                ordenarQuantidade()

        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida.")