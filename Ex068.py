# LISTA 03
# 9) Crie uma lista de palavras e concatene em uma unica
# string
mainString = ''
while True:
    palavra = input('Digite uma palavra: ')
    mainString = '' + mainString + '' + palavra

    continuar = int(input('Deseja continuar 1-Sim 0- Nao: '))
    if continuar == 0:
        break

print(f'A frase formada é: "{mainString}"')