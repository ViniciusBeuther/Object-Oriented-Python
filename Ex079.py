#LISTA 04
# 8) Receba uma quantidade x de numeros e retorne com uma funcao a media
# dos numeros, caso digite fim termina

def media(soma,i):
    return soma/i

i = 0
L = []
soma = 0
while True:
    number =input('Digite um numero ou "Fim" para encerrar: ')
    if number.isdigit() == True:
        i+=1
        aux = float(number)
        soma += aux
    else:
        if number.upper() == 'FIM':
            break
print(f'A media dos valores digitados é {media(soma,i)}')


