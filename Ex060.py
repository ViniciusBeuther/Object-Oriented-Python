# LISTA 03
# 1) Crie uma lista de números inteiros e exiba o valor máximo e mínimo.
L = []
maior = -999999999
menor = 9999999999
i=0
while True:
    L.append(int(input('Digite um numero: ')))
    if L[i] > maior:
        maior = L[i]
    if L[i] < menor:
        menor = L[i]
    i+=1
    continuar = int(input('Deseja continuar: 1-Sim 0-Não: '))
    if continuar is 0:
        break

print(f'O maior numero é {maior} e o menor é {menor}')
