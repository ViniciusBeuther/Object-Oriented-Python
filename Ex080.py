#LISTA 04
# 09) Faca uma funcao chamada procura que recebe uma lista
# e um nome, retorna True se encontrar o nome ou False se nao encontrar

def procurar(lista, nome):
    status = 'False'
    for e in lista:
        if e == nome:
            status = 'True'
            break
        else:
            status = 'False'
    return status

L = []
while True:
    nomes = input('Digite um  (0-Encerra): ')
    if nomes == '0':
        break
    L.append(nomes)

nome = input('Digite o nome que deseja procurar: ')
print(f'\n{procurar(L,nome)}')