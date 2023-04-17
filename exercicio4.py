import random

while True:
    numero_aleatorio = random.randint(1, 9)
    tentativa = 0

    while tentativa != numero_aleatorio:
        tentativa = int(input("Digite um número entre 1 e 9 (ou digite 'sair' para sair): "))

        if tentativa == 'sair':
            print("Obrigado por jogar! Até mais!")
            break

        if tentativa < numero_aleatorio:
            print("Tentativa menor do que o número correto.")
        elif tentativa > numero_aleatorio:
            print("Tentativa maior do que o número correto.")
        else:
            print("Parabéns! Você acertou o número!")
            break
