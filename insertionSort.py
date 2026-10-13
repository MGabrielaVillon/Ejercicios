import random
import time

def insertion_sort(A):
    # Implementación propia basada en el pseudocódigo de Cormen et al.
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

# 1. Definimos los tamaños
tamanos = [10, 100, 1000, 10000, 100000]

for n in tamanos:
    lista_original = [random.randint(1, 1000000) for _ in range(n)]
    
    # 2. Esta lista empieza vacía en cada tamaño y se llena sola
    tiempos_individuales = []
    
    repeticiones = 1 if n >= 100000 else 3
    
    for i in range(repeticiones):
        lista_a_ordenar = lista_original.copy()
        
        inicio = time.perf_counter()
        insertion_sort(lista_a_ordenar)
        fin = time.perf_counter()
        
        # Aquí el código guarda los tiempos automáticamente
        tiempos_individuales.append(fin - inicio)
    
    tiempo_promedio = sum(tiempos_individuales) / len(tiempos_individuales)
    
    # 3. Formateo automático de las columnas e1, e2, e3 y promedio
    e1 = f"{tiempos_individuales[0]:.4e}"
    e2 = f"{tiempos_individuales[1]:.4e}" if len(tiempos_individuales) > 1 else "        -"
    e3 = f"{tiempos_individuales[2]:.4e}" if len(tiempos_individuales) > 2 else "        -"
    prom = f"{tiempo_promedio:.4e}"
    
    print(f"{n:<22}{e1:<18}{e2:<18}{e3:<18}{prom:<18}")