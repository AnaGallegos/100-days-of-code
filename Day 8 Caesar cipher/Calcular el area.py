import math

def pintar(h, a):
    return h * a / 5


h = int(input('Altura: '))
a = int(input('Anchura: '))
print(math.ceil(pintar(h, a)))
