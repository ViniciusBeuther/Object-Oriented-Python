#Verificar um emprestimo bancario, entrar com valor da casa, salario e tempo a pagar (anos), e ver se aceita
# ou nao, não pode ultrapassar 30% da renda

valorCasa = float(input('Qual o valor da casa que deseja comprar (R$): R$ '))
valorSalario = float(input('Qual o valor do seu salário (R$): R$ '))
tempo = int(input('Em quantos anos deseja pagar a casa: '))

limiteParcela = valorSalario * 0.3
parcela = valorCasa/(tempo*12)

if tempo <= 0:
    print('ANO INVÁLIDO! TENTE NOVAMENTE!')
else:
    if parcela > limiteParcela:
        print(f'O financiamento não foi aprovado! O valor ultrapassa 30% de sua renda, sendo mais de R$ {limiteParcela:.2f}')
    else:
        print(f'O financiamento foi aprovado! O valor não ultrapassa 30% de sua renda mensal! PARABÉNS!')
