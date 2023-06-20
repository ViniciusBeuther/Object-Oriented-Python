#LISTA 04
# 7) Crie uma funcao que retorne uma lista digitado invertida

def inverte(lista, qtd):
    inversa = []
    quantidadeNumeros = len(lista)

    for e in lista[::-1]:
            inversa.append(e)
    return inversa

i=0
L = []
while True:
    L.append(int(input('Digite um numero: ')))
    i+=1
    parar = int(input('Continuar 1-Sim 0-Nao: '))
    if parar is 0:
        break
print(f'O valor invertido {inverte(L, i)}')

