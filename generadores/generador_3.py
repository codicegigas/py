def numeros_inifinitos():
    n = 1
    while True:
        yield n
        n += 1

for numero in numeros_inifinitos():
    if numero > 5:
        break
    print(numero)   