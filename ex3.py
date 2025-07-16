from functools import reduce

def analisa_listas(*listas: list):
    result = sum(reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, lista)) for lista in listas)
    return result

# Exemplo de uso:

lista1 = [1,2,3,4]
lista2 = [5,6,8,9]
lista3 = [10,11,12,13]

print(analisa_listas(lista1, lista2, lista3))
