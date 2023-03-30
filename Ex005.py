#Escreva um programa que leia dois numeros e que escolha a operação a ser realizada

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
escolha = int(input('\n1-Soma\n2-Subtração\n3-Divisão\n4-Multiplicação\nQual operação deseja:'))

if escolha == 1:
    resultado = n1 + n2
elif escolha == 2:
    resultado = n1 - n2
elif escolha == 3:
    resultado = n1/n2
elif escolha == 4:
    resultado = n1*n2
else:
    print('Escolha inválida!')
print(f'A operação escolhida foi {escolha}, o resultado é: {resultado:.2f}')