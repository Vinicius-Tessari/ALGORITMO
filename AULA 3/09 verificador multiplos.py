try:
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    if b == 0:
        print("Valor inválido para b.")
    else:
        if a % b == 0:
            print("a é múltiplo de b")
        else:
            print("a não é múltiplo de b")
except ValueError:
    print("Entrada inválida.")
