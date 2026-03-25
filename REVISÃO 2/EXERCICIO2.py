opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        print("Cadastrar selecionado")
    case 2:
        print("Alterar selecionado")
    case 3:
        print("Excluir selecionado")
    case 4:
        print("Sair selecionado")
    case _:
        print("Opção inválida")