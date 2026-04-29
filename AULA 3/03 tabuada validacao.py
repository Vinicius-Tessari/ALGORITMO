try:
    n = int(input("Digite um número inteiro: "))
    if n < 0:
        print("Número inválido")
    else:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
except ValueError:
    print("Entrada inválida.")
