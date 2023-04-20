#LISTA 02
#4) Faça um programa que calcule se um ano é
# ou não bissexto (se necessário, procure a regra na Internet)

ano = int(input('Digite um ano: '))
if ano < 0:
    print('Ano inválido!')
else:
    if ano % 4 == 0 and ano % 400 != 0 and ano % 100 != 0:
        print('O ano digitado é BISSEXTO!')
    else:
        print('O ano não é BISSEXTO!')
