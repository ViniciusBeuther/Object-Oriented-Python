#desenvolva um programa para calcular o custo
# e quantas latas de tintas serão utilizados para
# pintar tanques
#  cilíndricos de combustível sendo que:
#   - a lata de tinta custa R$120,00
#   - cada lata contém 5 litros
#   - cada litro pinta 4m²
#   - a altura e o raio do tanque serão informados pelo usuário
#   - mostre na tela a área do tanque, a quantidade de latas e o custo total

from math import ceil
h = float(input('Digite a altura do tanque: '))
r = float(input('Digite o raio do tanque: '))
areaTanque = (3.14 * pow(h,2)) * h

print('\n-----INFORMAÇÕES-----')

if h < 0 or r < 0:
    print('Valores inválidos, encerrando...')
else:
    litrosTinta = areaTanque/4
    latas = ceil(areaTanque/20)
    print(f'Area do tanque = {areaTanque} m2\nTotal de tinta = {litrosTinta:.2f}L\nNumero de latas: {latas}\nTotal: R${latas*120:.2f}')