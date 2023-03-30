#Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a
#média é ponderada e que o peso das notas é: 2,3 e 5,
#respectivamente.

n1 = float(input('Digite a nota 01: '))
n2 = float(input('Digite a nota 02: '))
n3 = float(input('Digite a nota 03: '))
media = (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)
if media < 7:
    print('Voce foi reprovado! Média geral: {:.2f}'.format(media))
else:
    print('Aprovado! Média geral: {:.2f}'.format(media))
