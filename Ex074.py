# LISTA4 - FUNCOES
# receba 4 notas e retorne a media

def media(notas):
    soma = 0
    for e in notas:
        soma += e
    return (soma/len(notas))

notas = []
i = 0
while i < 4:
    notas.append(float(input(f'Digite a nota {i+1}: ')))
    i+=1

print(f'A média das notas digitadas é {media(notas):.2f}')