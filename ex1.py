def candidatos_aptos(candidatos: list):
    result = [
        nome
        for nome, idade in candidatos
        if idade >= 18
    ]
    return result

# Exemplo de uso:

lista_candidatos = [
    ('João', 18),
    ('Pedro', 10),
    ('Paulo', 24),
    ('Felippe', 16),
]

print(candidatos_aptos(lista_candidatos)) # ['João', 'Paulo']