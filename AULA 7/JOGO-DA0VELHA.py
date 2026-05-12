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

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Essa posição já está ocupada. Escolha outra.")
        return False

    return True


def fazer_jogada(tabuleiro, posicao, jogador):
    posicao = int(posicao)

    linha = (posicao - 1) // 3
    coluna = (posicao - 1) % 3

    tabuleiro[linha][coluna] = jogador


def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha[0] == jogador and linha[1] == jogador and linha[2] == jogador:
            return True

    for coluna in range(3):
        if (
            tabuleiro[0][coluna] == jogador and
            tabuleiro[1][coluna] == jogador and
            tabuleiro[2][coluna] == jogador
        ):
            return True

    if (
        tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador
    ):
        return True

    if (
        tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador
    ):
        return True

    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor not in ["X", "O"]:
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

    jogador_atual = "X"
    jogo_ativo = True

    print("Bem-vindo ao Jogo da Velha!")

    while jogo_ativo:
        mostrar_tabuleiro(tabuleiro)

        posicao = input(f"Jogador {jogador_atual}, escolha uma posição: ")

        if validar_jogada(tabuleiro, posicao):
            fazer_jogada(tabuleiro, posicao, jogador_atual)

            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                jogo_ativo = False

            elif verificar_empate(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("O jogo terminou empatado!")
                jogo_ativo = False

            else:
                jogador_atual = trocar_jogador(jogador_atual)

jogar()