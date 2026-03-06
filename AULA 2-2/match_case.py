opcao = int(input("Digite uma opção (1-3): "))

match opcao:
    case 1:
        print("Você escolheu 1")
    case 2:
        print("Você escolheu 2")
    case 3:
        print("Você escolheu 3")
    case _:
        print("Opção inválida")