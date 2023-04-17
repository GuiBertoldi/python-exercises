palavra = input("Digite uma palavra: ")

palavra = palavra.lower()
palavra = palavra.replace(" ", "")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra", palavra, "é um palíndromo!")
else:
    print("A palavra", palavra, "não é um palíndromo.")