#Receber 2 número e imprimir a soma, a subtração,
#multiplicação e divisão entre eles.

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
print(f'A soma de {n1:.2f} + {n2:.2f} = {n1+n2:.2f}')
print(f'A subtração de {n1:.2f} - {n2:.2f} = {n1-n2:.2f}')
print(f'A divisão de {n1:.2f} por {n2:.2f} = {n1/n2:.2f}')
print(f'A multiplicação de {n1:.2f} por {n2:.2f} = {n1*n2:.2f}')