soma = 0
quantidade = 0

while True:
    entrada = input("Digite um número inteiro (0 para sair): ")
    try:
        numero = int(entrada)
        if numero == 0:
            break
        else:
            soma += numero
            quantidade += 1
    except ValueError:
        print("Entrada inválida.")

print(f"Soma dos números: {soma}")
print(f"Quantidade de números digitados: {quantidade}")
