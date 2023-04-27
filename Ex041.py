#Criando média com vetores
n = int(input('Digite o numero de notas: '))
notas = []
soma = 0
valor = []

for i in range(0,n,1):
    valor = float(input(f'Digite a nota {i+1}: '))
    notas.append(valor)
    soma+=valor

print(f'As notas digitadas são {notas}')
print(f'A média das notas é: {soma/n:.2f}')