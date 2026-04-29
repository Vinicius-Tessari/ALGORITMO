try:
    n = int(input("Digite um inteiro maior ou igual a 1: "))
    if n < 1:
        print("Valor inválido.")
    else:
        pares = 0
        impares = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                pares += 1
            else:
                impares += 1
        print(f"Pares: {pares}")
        print(f"Ímpares: {impares}")
except ValueError:
    print("Entrada inválida.")
