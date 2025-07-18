from functools import reduce

def soma_pares(*listas: list):
    for lista in listas: 
        if lista == []: return 'Não insira listas vazias'

    try:
        result = sum(reduce(lambda x, y: x + y, filter(lambda num: num % 2 == 0, lista)) for lista in listas)
        return result
    except:
        print('Erro: Insira listas válidas!')

# Exemplo de uso:

lista1 = [1,2,3,4]
lista2 = [5,6,8,9]
lista3 = [10,11,12,13]

print(soma_pares(lista1, lista2, lista3)) # 42
