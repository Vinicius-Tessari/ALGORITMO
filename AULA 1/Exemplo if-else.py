numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

operacao = input("Qual operação você quer? (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", numero1 + numero2)

elif operacao == "-":
    print("Resultado:", numero1 - numero2)

elif operacao == "*":
    print("Resultado:", numero1 * numero2)

elif operacao == "/":
    if numero2 == 0:
        print("Não dá pra dividir por zero")
    else:
        print("Resultado:", numero1 / numero2)
else:
    print("Essa operação não existe")
