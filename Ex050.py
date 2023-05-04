# Escrever um programa que leia 5 números float e imprima-os
# em ordem inversa.

vetor = []
i = 0
while i < 5:
    vetor.append(float(input('Digite um numero: ')))
    i+=1
print('Os valores do vetor invertido são: ')
vetor.reverse()

print(vetor)


