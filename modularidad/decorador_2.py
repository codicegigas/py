# modularidad/decorador_2.py
# Decorador para medir el tiempo de ejecución de una función
#medir_tiempo calcula cuanto tarda en ejecutarse una función
#contar hace un ciclo grande y el decorador mide el tiempo que tarda en ejecutarse
# Asi el decorador nos da informacion adicional sin modificar el código original de contar
import time

def medir_tiempo(funcion):
    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f"Tiempo: {fin - inicio:.4f} segundos")
    return wrapper

@medir_tiempo
def contar():
    suma = 0
    for i in range(1000000):
        suma += i
    print("Suma lista")

contar()

