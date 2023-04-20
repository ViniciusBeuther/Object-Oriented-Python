#LISTA 02
# 6) Faça um programa que leia a idade e a altura de uma pessoa e verifique se
# ela pode entrar em um parque de diversões. Para entrar no parque,
# a pessoa deve ter pelo menos 12 anos e medir mais de 1,50m.

altura = float(input('Digite sua altura (m): '))
idade = int(input('Digite sua idade: '))

if altura <= 0 or idade < 0:
    print('Valores inválidos!')
else:
    if altura > 1.5 and idade >= 12:
        print('Voce pode entrar no parque de diversões!')
    else:
        print('Voce nao pode entrar no parque de diversões!')