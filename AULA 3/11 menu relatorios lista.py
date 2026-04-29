numeros = []

while True:
    print("\n1) Adicionar número na lista")
    print("2) Mostrar maior número")
    print("3) Mostrar menor número")
    print("4) Mostrar soma total")
    print("0) Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            try:
                numero = float(input("Digite um número: "))
                numeros.append(numero)
                print("Número adicionado.")
            except ValueError:
                print("Entrada inválida.")
        case "2":
            if len(numeros) == 0:
                print("Lista vazia.")
            else:
                maior = numeros[0]
                for numero in numeros:
                    if numero > maior:
                        maior = numero
                print(f"Maior número: {maior}")
        case "3":
            if len(numeros) == 0:
                print("Lista vazia.")
            else:
                menor = numeros[0]
                for numero in numeros:
                    if numero < menor:
                        menor = numero
                print(f"Menor número: {menor}")
        case "4":
            if len(numeros) == 0:
                print("Lista vazia.")
            else:
                soma = 0
                for numero in numeros:
                    soma += numero
                print(f"Soma total: {soma}")
        case "0":
            print("Encerrando o programa.")
            break
        case _:
            print("Opção inválida.")
