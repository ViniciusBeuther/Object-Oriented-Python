# A lista de temperaturas de Mons, na Bélgica, foi armazenada na
# lista T = [-10, -8, 0, 1, 2, 3, -2, -4]. Faça um programa que
# imprima a menor e a maior temperatura, assim como a
# temperatura média.

i = 0
T = [-10, -8, 0, 1, 2, 3, -2, -4]
menor = 9999999999
maior = -999999999
soma = 0

for e in T:
    if e > maior:
        maior = e
    if e < menor:
        menor = e
    soma+=e

print('-----DADOS SOBRE TEMPERATURA NA BELGICA-----')
print(f'Maior: {maior}ºC')
print(f'Menor: {menor}ºC')
print(f'Media: {soma/len(T):.2f}ºC')