try:
    qtd = int(input("Quantas notas você vai digitar? "))
    if qtd <= 0:
        print("Quantidade inválida.")
    else:
        soma = 0
        for i in range(qtd):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1}: "))
                    if 0 <= nota <= 10:
                        soma += nota
                        break
                    else:
                        print("Nota inválida. Digite uma nota entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida.")
        media = soma / qtd
        print(f"Média: {media:.2f}")
except ValueError:
    print("Entrada inválida.")
