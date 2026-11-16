"""Ejercicio 3: capturar diez notas, ordenar con burbuja y buscar con binaria."""


def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista


def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


def pedir_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 100:
                return nota
            print('La nota debe estar entre 0 y 100.')
        except ValueError:
            print('Error: ingrese un número válido.')
        except EOFError:
            raise SystemExit('No se recibieron más datos de entrada.')


def main():
    notas = []
    print('REGISTRO DE 10 NOTAS')
    for i in range(10):
        notas.append(pedir_nota(f'Ingrese la nota {i + 1}: '))

    burbuja(notas)
    print('\nNotas ordenadas:')
    print(notas)

    objetivo = pedir_nota('\nNota que desea buscar: ')
    posicion = busqueda_binaria(notas, objetivo)
    if posicion != -1:
        print(f'La nota {objetivo:g} existe.')
        print(f'Se encuentra en el índice {posicion} (posición {posicion + 1}).')
    else:
        print(f'La nota {objetivo:g} no existe.')


if __name__ == '__main__':
    main()
