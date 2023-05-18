#LISTA 4 - FUNCOES
# 2) Fazer uma funcao que receba como parametro um numero int
# e retorne o fatorial desse numero

def fatorial(a):
    fatorial = 1
    while a > 0:
        fatorial = fatorial * a
        a-=1
    return (fatorial)

a = int(input('Digite um numero inteiro: '))
print(f'Fatorial é {fatorial(a)}')
