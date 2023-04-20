#LISTA 02
# 7) Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('Digite o numero 1: '))
n2 = float(input('Digite o numero 2: '))

if n1 > n2:
    maior = n1
else:
    maior = n2

print(f'O maior numero é {maior}')