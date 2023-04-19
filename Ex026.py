#crie um algoritmo que leia dois números inteiros e depois mostre:
   #- o primeiro valor vezes o segundo
   # o segundo valor menos o primeiro
   #- o inverso do primeiro valor vezes o segundo multiplicado por 5
   #- o quadrado do primeiro dividido pelo segundo elevado a -2

num1 = int(input('Digite o primeiro numero (Inteiro) :'))
num2 = int(input('Digite o segundo numero (Inteiro) :'))

print(f'O numero {num1} x {num2} é igual a {num1*num2:.2f}.')
print(f'O numero {num2} - {num1} é igual a {num2-num1}.')
print(f'O inverso do primeiro x o segundo é igual a {(num1 * -1) * (num2 * 5)}')
print(f'O quadrado de ({num1} / {num2}) elevado a -2 é igual a: {pow((num1/num2), -2)}')