# Valor inicial da divida | juro mensal | numero de meses
# total == valorInicial + (valorInicial * (Juros/100))
# Total da divida

valorInicial = float(input('Digite o valor inicial da divida: R$ '))
valorJuro = float(input('Digite a taxa de juros mensais (%): '))
meses = int(input('Digite o numero de meses para pagar: '))
valorFinal = valorInicial
i = 1
print('\n')

# Condições inválidas
if valorInicial < 0:
    print('Voce não possui uma divida!')

elif valorJuro < 0 or meses <= 0:
    print('Valores INVÁLIDOS!')
# Processando os dados corretos
else:
    while i <= meses:
        valorFinal += (valorFinal * (valorJuro / 100))
        print(f'{i}º mês sua divida estará em R$ {valorFinal:.2f}')
        i+=1
print(f'O valor final da divida é de R$ {valorFinal:.2f}')
print(f'Você pagará um total de R$ {valorFinal-valorInicial:.2f} de JUROS!')
