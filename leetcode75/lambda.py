
# lambda args: expressão
# ex 
f = lambda x : x + 2

# 1. Com map() – Transforma cada item de um iterável
# dados = [1, 2, 3, 4]
# transformados = map(lambda x: x * 2, dados)
# print(list(transformados))  # [2, 4, 6, 8]


# 2. Com filter() – Filtra com base numa condição
dados = [1, 2, 3, 4, 5]
# pares = filter(lambda x: x % 2 == 0, dados)
# print(list(pares))  # [2, 4]
from functools import reduce

reduced = reduce(lambda x, y: x + y, dados)
print(reduced)

# nomes = ['Ana', 'Bruno', 'Carlos']
# ordenado = sorted(nomes, key=lambda nome: nome[-1])
# print(ordenado)  # ['Ana', 'Bruno', 'Carlos'] → ordenado pelo último caractere

# pop() and insert(), reduce() etc... operations increase the complexity by O(n) each

def reverse_number(number: int):
    rev = 0
    sign = 1 if number > 0 else -1
    while number:
        mod = number % 10
        number = number // 10
        rev = rev * 10 + mod
    return rev * sign

print(reverse_number(123))