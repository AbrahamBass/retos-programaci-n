
# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS
# las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def main(p1: str, p2: str):
    if p1 == p2:
        return "Las dos palabras no pueden ser iguales:)"

    list1 = list(p1)
    list2 = list(p2)

    list1.sort()
    list2.sort()

    ord1 = "".join(list1)
    ord2 = "".join(list2)

    print(ord1)
    print(ord2)

    return ord1 == ord2

print(main(input('Palabra 1: ').lower(),p2 = input('Palabra 2: ').lower()))
