try:
    n = int(input("Digite a quantidade de termos: "))
    if n < 1:
        print("Valor inválido.")
    else:
        a = 0
        b = 1
        for i in range(n):
            if i == 0:
                print(a)
            elif i == 1:
                print(b)
            else:
                c = a + b
                print(c)
                a = b
                b = c
except ValueError:
    print("Entrada inválida.")
