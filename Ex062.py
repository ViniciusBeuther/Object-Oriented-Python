# LISTA 03
# 3) Crie uma lista de números e ordene do menor para o maior.

L=[2,1,5,4,7, 12, 57, 1, -10]
fim = len(L)
while fim > 1:
    trocou=False
    x = 0
    while x<(fim-1):
        if L[x] > L[x+1]:
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
            trocou = True
        x += 1
    if not trocou:
        break
    fim -= 1
print(f'A lista ordenada do menor para o maior:')
print(L)