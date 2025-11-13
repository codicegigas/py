def cuadrados(n):
    for i in range(n):
        yield i ** 2

for numero in cuadrados(10):
    print(numero)