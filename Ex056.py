# Faça um programa para imprimir o menor elemento de uma lista.
L = []
i = 0
menor = 99999999999999999999999999

while True:
    num = int(input('Digite um numero para adicionar na lista: '))
    L.append(num)
    continuar = int(input('Deseja continuar 1-SIM 0-NAO: '))
    if L[i] < menor:
        menor = L[i]
        i+=1

    else:
        i+=1

    if continuar == 0:
        break
print(f'O menor numero é {menor}')

