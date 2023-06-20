#LISTA 04
#6) Criar uma funcao que recebe uma lista e retorna o valor maximo da lista

def maximo(lista):
    maior = lista[0]
    for e in lista:
        if e > maior:
            maior = e
    return maior

L = [1,2,3,4,5,6,11,25,67,98,20]

print(f'O maior valor da lista é {maximo(L)}')