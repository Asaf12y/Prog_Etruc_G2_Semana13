# Algoritmos de búsqueda y ordenamiento en Python

Cinco ejercicios de programación estructurada para practicar el algoritmo **burbuja**, la **búsqueda binaria** y el análisis de **complejidad Big O**.

## Contenido

| Archivo | Descripción |
| --- | --- |
| `ejercicio_1_traza_burbuja.py` | Traza de `[9, 7, 5, 3, 1]`: 10 comparaciones, 10 intercambios; peor caso. |
| `ejercicio_2_burbuja_descendente.py` | Ordena de mayor a menor. |
| `ejercicio_3_notas_busqueda_binaria.py` | Solicita 10 notas (0 a 100), las ordena y busca una nota mediante búsqueda binaria. |
| `ejercicio_4_burbuja_nombres.py` | Ordena alfabéticamente una lista de nombres. |
| `ejercicio_5_tiempos_burbuja.py` | Compara el tiempo de ejecución para 1000, 2000 y 4000 elementos aleatorios. |

## Requisitos

- Python 3.8 o superior.
- No se necesitan librerías externas: solo se usan las bibliotecas estándar `random` y `time` en el ejercicio 5.

## Ejecución

Desde la terminal, dentro de la carpeta del proyecto:

```bash
python ejercicio_1_traza_burbuja.py
python ejercicio_2_burbuja_descendente.py
python ejercicio_3_notas_busqueda_binaria.py
python ejercicio_4_burbuja_nombres.py
python ejercicio_5_tiempos_burbuja.py
```

En algunos sistemas el comando puede ser `python3` en lugar de `python`.

## Complejidad

- **Burbuja básica:** O(n²) en comparaciones; O(1) memoria auxiliar.
- **Burbuja optimizada:** mejor caso O(n), peor caso O(n²).
- **Búsqueda binaria:** O(log n), requiere lista ordenada.
- **Ejercicio 3 completo:** O(n²), dominado por el ordenamiento.

## Cómo subir a GitHub

1. Crea un repositorio nuevo en GitHub.
2. Selecciona **Add file → Upload files**.
3. Arrastra los archivos de esta carpeta (incluido el `README.md`).
4. Haz clic en **Commit changes**.

También puedes hacerlo desde la terminal:

```bash
git init
git add .
git commit -m "Agregar ejercicios de búsqueda y ordenamiento"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
```

Reemplaza `TU_USUARIO` y `TU_REPOSITORIO` por los datos reales de tu cuenta.
