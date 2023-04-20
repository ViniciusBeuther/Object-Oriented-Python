#LISTA 02
# 5) Faça um programa que leia duas notas de um aluno e
# calcule a média. Se a média for maior ou igual a 6

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2 : '))
media = (n1+n2)/2
if media < 7:
    print(f'A media do aluno foi {media:.2f}, sendo inferior a 7!')

else:
    print(f'A media do aluno foi {media:.2f}, sendo acima de 7!')