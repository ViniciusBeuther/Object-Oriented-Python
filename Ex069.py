# LISTA 03
# 10) Crie uma lista de numeros e encontre a diferença entre o maior
# e menor numero dela

def media(maior,menor):
    return ((maior+menor)/2)

numeros = []
maior = -999999999999
menor = 9999999999999
while True:
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    continuar = int(input('Deseja continuar 1-Sim 0-Nao: '))
    if continuar == 0:
        break

print(media(maior,menor))

