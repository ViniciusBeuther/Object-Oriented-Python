# Faça um programa que leia duas listas e que gere uma terceira
# com os elementos das duas primeiras.

A = []
B = []
C = []
i=0
while True:
    A.append(int(input('Digite um numero A: ')))
    B.append(int(input('Digite um numero B: ')))
    C.append(A[i])
    C.append(B[i])
    i+=1
    continuar = int(input('Deseja continuar 1-Sim 0-Nao: '))
    if continuar == 0:
        break
print("Vetor C[A + B]: ", C)