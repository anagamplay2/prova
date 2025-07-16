def calcula_desconto(produtos: list, **opcoes):
    if produtos == []: return 'Nenhum produto cadastrado'
    
    desconto = opcoes.get('desconto', 0)/100

    return [
        (p.get('nome', ''), p.get('preco', 0) - p.get('preco', 0) * desconto)
        for p in produtos
    ]

# Exemplo de uso:

lista_produtos = [
    {"nome": "Batata", "preco": 100},
    {"nome": "Maçã", "preco": 200},
    {"nome": "Laranja", "preco": 50},
    {"nome": "Uva", "preco": 120}
] 

print(calcula_desconto(lista_produtos))