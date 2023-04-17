while True:
    print("Jogador 1: Pedra, Papel ou Tesoura?")
    jogador1 = input("Digite sua jogada: ").lower()
    print("Jogador 2: Pedra, Papel ou Tesoura?")
    jogador2 = input("Digite sua jogada: ").lower()

    if jogador1 == jogador2:
        print("Empate!")
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra"):
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

    continuar = input("Deseja continuar jogando? (s/n): ").lower()
    if continuar != "s":
        break