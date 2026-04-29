while True:
    print("\n1) Celsius para Fahrenheit")
    print("2) Fahrenheit para Celsius")
    print("0) Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            valor = input("Digite a temperatura em Celsius: ")
            try:
                c = float(valor)
                f = (c * 9 / 5) + 32
                print(f"Resultado: {f:.2f}")
            except ValueError:
                print("Entrada inválida.")
        case "2":
            valor = input("Digite a temperatura em Fahrenheit: ")
            try:
                f = float(valor)
                c = (f - 32) * 5 / 9
                print(f"Resultado: {c:.2f}")
            except ValueError:
                print("Entrada inválida.")
        case "0":
            print("Encerrando o programa.")
            break
        case _:
            print("Opção inválida.")
