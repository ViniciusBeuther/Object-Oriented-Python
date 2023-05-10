# LISTA 03
# 8) Crie uma lista de numeros e encontre a média

L = [10,7,8,5,3,9]
def media (Lista):
    soma = 0
    for e in Lista:
        soma+=e
    return (soma/len(Lista))

print(f'O valor da média é {media(L)}')