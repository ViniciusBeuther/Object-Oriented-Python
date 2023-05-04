# Ler e armazenar num vetor 5 números float fornecidos pelo
# usuário e calcular a média dos valores.

valores = []
i = 0
soma = 0
while i < 5:
    valores.append(float(input(f'Digite o valor {i+1}: ')))
    i+=1
for e in valores:
    soma+=e
print(f'A média entre os valores fornecidos é {soma/(len(valores)):.2f}')