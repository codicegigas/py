# List Comprehension


rango = [x for x in range(20)]

rango2 = []

for x in range(20):
    rango2.append(x)


print(rango)
print(rango2)

# Dictionary Comprehension

from string import ascii_uppercase #aLMACENA EL ALFABETO MAYUSCULA

alphabet = {k:v for k,v in zip([x for x in range(1,27)], ascii_uppercase)}

print(alphabet)