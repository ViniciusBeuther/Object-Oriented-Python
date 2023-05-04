# Faça um programa que percorra duas listas e gere uma terceira
# sem elementos repetidos.
i = 0
A = []
B = []
C = []

while True:
    A.append((int(input('Digite um elemento A: '))))
    B.append(int(input('Digite um elemento B: ')))
    i+=1

    continuar = int(input('Deseja contiuar 1-Sim 0-Nao: '))

    if continuar == 0:
        break

for e in A+B:
    if e not in C:
        C.append(e)
print(C)
