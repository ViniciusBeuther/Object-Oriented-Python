# FUNCTIONS
# Faça um programa com uma funcao que precise de 3 argumentos
# e que forneça a soma deles

def soma(num1, num2, num3):
    soma=num1+num2+num3
    return (soma)

n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))

print(f'O valor da soma é: {soma(n1,n2,n3)}')