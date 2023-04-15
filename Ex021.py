#Verificar se o numero é primo
num = int(input('Digite um numero para ver se é primo: '))
i = 3
flag = 0
while i < num:
    if num%i == 0:
        flag = 1
    else:
        i+=2

if flag == 1:
    print('Não é primo')
else:
    print('É primo')
