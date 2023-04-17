def remove_duplicatas(lista):

    elementos_unicos = set()

    for elemento in lista:
        elementos_unicos.add(elemento)

    lista_sem_duplicatas = list(elementos_unicos)

    return lista_sem_duplicatas

lista = ["Michele", "Ronaldo", "Sara", "Robin", "Michele", "Sara", "Lucas", "Ronaldo", "Pedro", "Michele", "Lucas", "Sara", "Ronaldo", "Maria", "Robin"]
lista_sem_duplicatas = remove_duplicatas(lista)
print("Lista original:", lista)
print("Lista sem duplicatas:", lista_sem_duplicatas)
