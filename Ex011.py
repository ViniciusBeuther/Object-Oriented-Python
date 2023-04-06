#Faça um programa para imprimir os numeros imapares de 0 até o digitado pelo usuario
max = int(input('Digite até que numero deseja ver os pares: '))
x = 0
while x <= max:
    if x%2 == 0:
        print(f'{x} ', end="")
    x+=1