#Ler numeros inteiros > 0 e depois mostrar o maior numero digitado até digitar 0
lista = []
maior = 0
while True:
    num = (int(input('Digite um numero (0 para encerrar): ')))
    lista.append(num)
    if num is 0:
        break

for e in lista:
    if e > maior:
        maior = e

print(f'O maior numero digitado é {maior}')