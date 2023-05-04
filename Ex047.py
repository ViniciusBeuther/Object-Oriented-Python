# Inicializar um vetor com valores 2, 4, 6, 8, 10. Calcular e
# imprimir a soma dos valores.
soma = 0
valores = [2, 4, 6, 8, 10]

for i in valores:
    soma += i
print(f'A média é de {soma/(len(valores)):.2f}')