fila = []
proxima_senha = 1

while True:
    print("\n1) Gerar senha")
    print("2) Chamar próxima senha")
    print("0) Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            fila.append(proxima_senha)
            print(f"Senha gerada: {proxima_senha}")
            proxima_senha += 1
        case "2":
            if len(fila) == 0:
                print("Fila vazia.")
            else:
                senha = fila.pop(0)
                print(f"Chamando senha: {senha}")
        case "0":
            print("Encerrando o programa.")
            break
        case _:
            print("Opção inválida.")
