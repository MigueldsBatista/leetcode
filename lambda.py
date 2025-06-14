
# lambda args: expressão
# ex 
f = lambda x : x + 2

# 1. Com map() – Transforma cada item de um iterável
# dados = [1, 2, 3, 4]
# transformados = map(lambda x: x * 2, dados)
# print(list(transformados))  # [2, 4, 6, 8]


# 2. Com filter() – Filtra com base numa condição
# dados = [1, 2, 3, 4, 5]
# pares = filter(lambda x: x % 2 == 0, dados)
# print(list(pares))  # [2, 4]


# nomes = ['Ana', 'Bruno', 'Carlos']
# ordenado = sorted(nomes, key=lambda nome: nome[-1])
# print(ordenado)  # ['Ana', 'Bruno', 'Carlos'] → ordenado pelo último caractere
