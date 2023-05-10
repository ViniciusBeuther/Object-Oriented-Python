# LISTA 03
# 2) Crie uma lista de nomes e ordene em ordem alfabética.
nomes = ['Vinicius', 'Carla', 'José', 'Carlito', 'Robson']
x=0

fim = len(nomes)
while fim > 1:
    trocou=False
    x = 0
    while x<(fim-1):
        if nomes[x] > nomes[x+1]:
            temp = nomes[x]
            nomes[x] = nomes[x+1]
            nomes[x+1] = temp
            trocou = True
        x += 1
    if not trocou:
        break
    fim -= 1
for e in nomes:
    print(e)