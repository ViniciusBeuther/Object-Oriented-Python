# Modifique o exercício anterior de forma a pesquisar p e v em
# toda a lista e informando ao usuário a posição onde p e a posição
# onde v foram encontrados.

L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar (P): '))
v = int(input('Digite outro valor a procurar (V): '))
i = 0
posicaoP = -1
posicaoV = -1

while i < len(L):
    if L[i] is p:
        posicaoP = i
        i+=1

    elif L[i] is v:
        posicaoV = i
        i+=1

    else:
        i+=1

print('-----INFO-----')
if posicaoP == -1:
    print('\nP nao encontrado')
else:
    print(f'\nO valor {p} foi encontrado na posição {posicaoP}')
if posicaoV == -1:
    print('V nao encontrado')
else:
    print(f'O valor {v} foi encontrado na posição {posicaoV}')


