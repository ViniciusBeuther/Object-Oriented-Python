# Faça um programa de forma a realizar a mesma tarefa do
# exemplo localizado no slide 21, mas sem utilizar a variável
# achou. Dica: observe a condição de saída do while.

L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
i = 0
while i < len(L):
    if L[i] is p:
        print(f'Valor encontrado na posição {i}!')
        break
    else:
        print(f'Nao encontrado na posição {i}')
        i+=1
