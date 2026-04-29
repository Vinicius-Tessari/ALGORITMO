while True:
    print("\n1) Somar")
    print("2) Subtrair")
    print("3) Multiplicar")
    print("4) Dividir")
    print("0) Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {a + b}")
            except ValueError:
                print("Entrada inválida.")
        case "2":
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {a - b}")
            except ValueError:
                print("Entrada inválida.")
        case "3":
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {a * b}")
            except ValueError:
                print("Entrada inválida.")
        case "4":
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                if b == 0:
                    print("Não é possível dividir por zero.")
                else:
                    print(f"Resultado: {a / b}")
            except ValueError:
                print("Entrada inválida.")
        case "0":
            print("Encerrando o programa.")
            break
        case _:
            print("Opção inválida.")
