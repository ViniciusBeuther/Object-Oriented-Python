#LISTA4 - FUNCOES
# 4) Receba 4 notas e seus respectivos pesos e mostre a media

def media (notas,peso):
    soma = 0
    somaNotas = 0
    i = 0
    while i < len(notas):
        soma += (notas[i] * (peso[i]))
        somaNotas += peso[i]
        i+=1
    return (soma/somaNotas)

peso = []
notas = []
i = 0
while i < 4:
    notas.append(float(input(f'Digite a nota {i+1}: ')))
    peso.append(float(input(f'Digite o peso {i+1}: ')))
    i+=1
print(f'A média foi de {media(notas, peso)}')
