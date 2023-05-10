# LISTA 03
# 4) Crie uma lista de palavras e crie uma nova lista com palavras que tem
# mais de 5 letras

L = []
Maior5 = []

while True:
    palavra = input('Digite uma palavra: ')
    if len(palavra) >= 5:
        Maior5.append(palavra)
    continuar = int(input('Deseja continuar 1-Sim 0-Não: '))
    if continuar == 0:
        break

print('\nPalavras digitadas > 5 caracteres: ')
print(Maior5)