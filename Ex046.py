# Ler 5 inteiros do teclado e armazenar num vetor. Depois
# percorrer este vetor mostrando os números ímpares.

impar = []
i = 0
while i < 5:
    num = int(input('Digite um numero inteiro: '))
    if num % 2 != 0:
        impar.append(num)
    i+=1
print('Os numeros impares digitados são:\n', impar)