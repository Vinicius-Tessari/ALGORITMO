a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

op = input("Operação desejada (+, -, *, /)").strip()

if op == "+":
    print("Resultado: ", a + b)
else:
    if op == "-":
        print("Resultado: ", a - b)
    else:
        if op == "*":
            print("Resultado: ", a * b)
        else:
            if op == "/":
                if b == 0:
                    print("Erro: divisão não pode ser por 0.")
                else:
                    print("Resultado: ", a / b)
            else:
                print("Operação inválida!!")        