# Ler 5 inteiros e armeznar em uma lista, mostrar somente os impares
impar = []
for i in range(0,5,1):
    n = int(input(f'Digite o numero {i+1}: '))
    if n % 2 != 0:
        impar.append(n)

for e in impar:
    print(e)
