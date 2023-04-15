# entrada = deposito inicial / taxa de juros
# processamento == valor final = valor final + deposito inicial + (deposito inicial * taxa)
# saida == num mes + valor final

depInicial = float(input('Deposito inicial: R$ '))
juros = float(input('Digite qual a taxa de juros mensal (%): '))
i = 1
saldoFinalMensal = depInicial

while i <= 12:
    saldoFinalMensal += (saldoFinalMensal * (juros/100))
    print(f'Mes {i}: {saldoFinalMensal:.2f}')
    i+=1

print(f'Você recebeu R${saldoFinalMensal-depInicial:.2f} em juros')
