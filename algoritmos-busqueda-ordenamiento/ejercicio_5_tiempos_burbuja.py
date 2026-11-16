"""Ejercicio 5: medir el tiempo de burbuja con 1000, 2000 y 4000 datos."""

import random
import time


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


def medir_tiempo(cantidad):
    numeros = [random.randint(1, 10000) for _ in range(cantidad)]
    inicio = time.perf_counter()
    burbuja(numeros)
    fin = time.perf_counter()
    return fin - inicio


def main():
    anterior = None
    for cantidad in [1000, 2000, 4000]:
        duracion = medir_tiempo(cantidad)
        print(f'Elementos: {cantidad} | Tiempo: {duracion:.6f} segundos')
        if anterior is not None and anterior > 0:
            print(f'Factor respecto al tamaño anterior: {duracion / anterior:.2f} veces')
        anterior = duracion
    print('\nAl duplicar n, el tiempo suele crecer aproximadamente 4 veces: O(n²).')
    print('Los tiempos dependen del equipo y de los datos aleatorios.')


if __name__ == '__main__':
    main()
