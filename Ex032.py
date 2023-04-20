#LISTA 02
#1) Faça um programa que verifique se uma pessoa é ou não maior de idade
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Maior de idade!')
elif idade < 18 and idade > 0:
    print('Menor de idade!')
else:
    print('Idade inválida!')