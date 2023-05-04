# Dado os vetores A=[10, 11, 12, 13, 14, 15, 16,17] e B=[1, 2, 3,
# 4, 5, 6, 7, 8], fazer um programa para somar os dois vetores e
# armazenar o resultado em um vetor C ( C[i]=A[i]+B[i] ).

A = [10,11,12,13,14,15,16,17]
B = [1,2,3,4,5,6,7,8]
C = []
i = 0
while i < len(A):
    C.append(A[i]+B[i])
    i+=1

print('A soma dos vetores A[i] + B[i] é: ')
for i, e in enumerate(C):
    print(f'C[{i}] = {e}')