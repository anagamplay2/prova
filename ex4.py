def retorna_saldo_final(registros: dict):
    if registros == None or registros == {}: return 'Nenhum registro cadastrado'

    result = {}
    for chave, valor in registros.items():
        saldo_final = 0
        for valor, tipo in valor:
            if tipo == 'entrada':
                saldo_final += valor
            else:
                saldo_final -= valor
        result[chave] = saldo_final 
    return result

# Exemplo de uso:

registros = {
    "alimentacao": [(1, 'entrada'), (2, 'saida')],
    "transporte": [(2, 'saida'), (3, 'saida')],
    "lazer": [(4, 'entrada'), (5, 'entrada')]
}

print(retorna_saldo_final(registros)) # {'alimentacao': -1, 'transporte': -5, 'lazer': 9}