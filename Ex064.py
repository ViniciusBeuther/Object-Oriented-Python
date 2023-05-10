# LISTA 03
# 5) Crie uma lista com numeros e outra com os pares

n = []
pares = []

while True:
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        pares.append(num)
    continuar = int(input('Deseja continuar 1-Sim 0-Nao: '))
    if continuar == 0:
        break

print(f'Os valores pares digitados são: ')
print(pares)