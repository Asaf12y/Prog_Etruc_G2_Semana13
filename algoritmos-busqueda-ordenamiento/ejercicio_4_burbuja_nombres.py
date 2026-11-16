"""Ejercicio 4: ordenar nombres alfabéticamente con burbuja."""


def burbuja_nombres(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j].casefold() > lista[j + 1].casefold():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def main():
    nombres = ['Jean', 'Emanuel', 'Jorge', 'Ana', 'Carlos']
    print('Nombres originales:', nombres)
    print('Nombres ordenados:', burbuja_nombres(nombres.copy()))
    print('Funciona porque Python permite comparar cadenas según sus caracteres Unicode.')
    print('casefold() evita diferencias entre mayúsculas y minúsculas.')
    print('Para ordenar acentos según las reglas del español se requieren ajustes adicionales.')


if __name__ == '__main__':
    main()
