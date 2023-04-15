#Usurio digita o numero que inicia e termina a tabuada
while True:
    inicio = int(input('Digite o valor inicial da tabuada: '))
    fim = int(input('Digite o valor final da tabuada: '))
    multiplicador = int(input('Digite o numero que deseja ver a tabuada: '))
    if fim > inicio:
        break
    print('Valor final maior que o inicial! Tente novamente! \n')
i = 0
while inicio <= fim:
    print(f'{multiplicador} x {inicio} = {multiplicador * inicio}')
    inicio+=1
