#Un generador es una funcion normal pero en vez de return usar yield
#Con yield la funcion recuerda en que parte se quedo y puede continuar la siguiente vez que se la llame
#Ejemplo:
#contar() es un generador que devuelve 1, 2 y 3 en cada llamada
#Cada vez que se ejecuta EL BUCLE en python obtiene el siguiente valor del generador
#Diferencia con return: si hubieramos usado return la funcion terminaria en el primer valor. Con yield se pausa y continua

def contar():
    yield 1
    yield 2
    yield 3

for numero in contar():
    print(numero)