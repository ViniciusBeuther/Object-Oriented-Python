#LISTA 4 - Funções
# 1) Fazer uma funcao que recebe 3 argumentos e retorna o
# produto desses elementos

def produto(a,b,c):
    produto = a*b*c
    return (produto)

a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))

print(f'O produto dos elementos é {produto(a,b,c):.2f}')
