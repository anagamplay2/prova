def calcula_desconto(produtos: list, **opcoes):
    if produtos == []: return 'Nenhum produto cadastrado'
    
    desconto = opcoes.get('desconto', 0)/100
    result = []
    for p in produtos:
        preco_atual = p.get('preco', 0)
        nome = p.get('nome', '')
        novo_preco = preco_atual - preco_atual * desconto if desconto != 0 else preco_atual
        result.append((nome, novo_preco))
    return result

# Exemplo de uso:

lista_produtos = [
    {"nome": "Batata", "preco": 10},
    {"nome": "Maçã", "preco": 2},
    {"nome": "Laranja", "preco": 5},
    {"nome": "Uva", "preco": 12}
] 

print(calcula_desconto(lista_produtos, desconto=10))
