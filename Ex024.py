#receba a temperatura em Celcius de um usuário
# e converta para Fahrenheit, exibindo o resultado na tela

temp = float(input('Digite a temperatura (ºC): '))
if temp < 0:
    print('Valor inválido!')
else:
    print(f'A temperatura de {temp} ºC em Fahrenheit é de {(temp*1.8)+32:.2f}')