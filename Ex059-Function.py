# faça uma funcao para buscar um valor em uma lista
def pesquise(lista,valor):
    for x, e in enumerate(lista):
        if e is valor:
            return x
    return None
# código
L = [1, 2, 3, 6, 9, 12, 5]
x = pesquise(L, 12)
print(L[x], ' na posição ', x)
print(pesquise(L, 4))