#Faça um programa para calcular e imprimir a media de 5 numeros digitados

i = 0
total = 0
while i < 5:
    num = float(input(f'Digite a nota {i}: '))
    total +=num
    i+=1

print(f'A média entre as 5 notas é {total/5:.2f}')
