def mostrar_tabuleiro(tabuleiro):
    print()
    for i, linha in enumerate(tabuleiro):
        print(f" {' | '.join(linha)}")
        if i < 2:
            print("-----------")
    print()

def validar_jogada(tabuleiro, posicao):
    if not posicao.isdigit():
        print("Digite apenas números de 1 a 9.")
        return False

    posicao = int(posicao)

    if posicao < 1 or posicao > 9:
        print("Posição inválida. Escolha um número de 1 a 9.")
        return False

    linha = (posicao - 1) // 3
    coluna = (posicao - 1) % 3

    if tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "O":
        print("Essa posição já está ocupada. Escolha outra.")
        return False

    return True

def fazer_jogada(tabuleiro, posicao, jogador):
    posicao = int(posicao)

    linha = (posicao - 1) // 3
    coluna = (posicao - 1) % 3

    tabuleiro[linha][coluna] = jogador

def verificar_vitoria(tabuleiro, jogador):
    if tabuleiro[0][0] == jogador and tabuleiro[0][1] == jogador and tabuleiro[0][2] == jogador:
        return True

    if tabuleiro[1][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[1][2] == jogador:
        return True

    if tabuleiro[2][0] == jogador and tabuleiro[2][1] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][0] == jogador and tabuleiro[2][0] == jogador:
        return True

    if tabuleiro[0][1] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][1] == jogador:
        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][2] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor != "X" and valor != "O":
                return False

    return True

def trocar_jogador(jogador):
    if jogador == "X":
        return "O"
    else:
        return "X"

def jogar():
    tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    jogador = "X"

    print("Bem-vindo ao Jogo da Velha!")

    while True:
        mostrar_tabuleiro(tabuleiro)

        posicao = input(f"Jogador {jogador}, escolha uma posição de 1 a 9: ")

        if validar_jogada(tabuleiro, posicao):
            fazer_jogada(tabuleiro, posicao, jogador)

            if verificar_vitoria(tabuleiro, jogador):
                mostrar_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                break

            if verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("O jogo terminou empatado!")
                break

            jogador = trocar_jogador(jogador)

jogar()