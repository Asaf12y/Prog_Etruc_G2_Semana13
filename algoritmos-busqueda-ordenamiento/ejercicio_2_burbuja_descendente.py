"""Ejercicio 2: ordenar números de mayor a menor con burbuja."""


def burbuja_descendente(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def main():
    numeros = [5, 3, 8, 4, 2]
    print('Lista original:', numeros)
    print('Lista ordenada de mayor a menor:', burbuja_descendente(numeros.copy()))


if __name__ == '__main__':
    main()
