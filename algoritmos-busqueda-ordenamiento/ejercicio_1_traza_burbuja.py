"""Ejercicio 1: traza de burbuja para una lista en orden inverso."""


def traza_burbuja(lista):
    numeros = lista.copy()
    comparaciones = 0
    intercambios = 0

    print('Lista inicial:', numeros)
    for i in range(len(numeros) - 1):
        comparaciones_pasada = 0
        intercambios_pasada = 0
        for j in range(len(numeros) - 1 - i):
            comparaciones += 1
            comparaciones_pasada += 1
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                intercambios += 1
                intercambios_pasada += 1
        print(f'Pasada {i + 1}: {numeros} | Comparaciones: {comparaciones_pasada} | Intercambios: {intercambios_pasada}')

    print('Total comparaciones:', comparaciones)
    print('Total intercambios:', intercambios)
    print('Caso: peor caso (lista inicialmente en orden inverso)')
    print('Complejidad temporal: O(n²)')
    return numeros


def main():
    traza_burbuja([9, 7, 5, 3, 1])


if __name__ == '__main__':
    main()
