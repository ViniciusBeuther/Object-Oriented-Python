# ler notas e encontrar a nota mais proxima da media
def media(notas):
    soma=0
    for e in notas:
        soma+=e
    media = soma/len(notas)
    if media < 0:
        media= media * (-1)
    return (media)
flag = 0
notas = []
i = 1
difMedia = 0
qtd = int(input('Quantas notas deseja adicionar?'))
while i <= qtd:
    notas.append(int(input(f'Digite a nota {i}: ')))
    i+=1

for x, e in enumerate(notas):
    if flag == 0:
        maisProximo = x
        difMedia = e-media(notas)
        flag = 1
    else:
        if (e-(media(notas))) > difMedia:
            maisProximo = x
            difMedia = e-media(notas)
print(f'O mais proximo é a nota {notas[x]}')
print(media(notas))
