try:
    qtd = int(input("Quantos alunos serão avaliados? "))
    if qtd <= 0:
        print("Quantidade inválida.")
    else:
        melhor_nome = ""
        melhor_nota = -1
        for i in range(qtd):
            nome = input(f"Digite o nome do aluno {i + 1}: ")
            while True:
                try:
                    nota = float(input(f"Digite a nota de {nome}: "))
                    if 0 <= nota <= 10:
                        break
                    else:
                        print("Nota inválida. Digite uma nota entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida.")
            if nota > melhor_nota:
                melhor_nota = nota
                melhor_nome = nome
        print(f"Aluno com maior nota: {melhor_nome}")
        print(f"Maior nota: {melhor_nota}")
except ValueError:
    print("Entrada inválida.")
