#LISTA 02
#2) Escreva um programa que receberá um número e dira se ele é positivo,
# negativo ou nulo

n = int(input('Digite um numero inteiro: '))
if n > 0:
    print('Numero é positivo.')
elif n < 0:
    print('Numero é negativo.')
else:
    print('Numero é neutro!')