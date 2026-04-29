while True:
    entrada = input("Digite um número inteiro positivo: ")
    try:
        numero = int(entrada)
        if numero > 0:
            print(f"OK: {numero}")
            break
        else:
            print("Valor inválido.")
    except ValueError:
        print("Entrada inválida.")
