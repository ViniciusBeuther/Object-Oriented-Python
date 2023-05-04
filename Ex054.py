# Modifique o exemplo (slide 21) para pesquisar dois valores. Em
# vez de apenas p, leia outro valor v que também será procurado.
# Na impressão, indique qual dos dois valores foi achado primeiro.

L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite outro valor a procurar: '))
i = 0
while i < len(L):
    if L[i] is p:
        print(f'Valor encontrado primeiro em P na posição {i}!')
        break
    elif L[i] is v:
        print(f'Valor encontrado primeiro em F na posição {i}!')
        break
    else:
        i+=1
