#LISTA 02
# 8) Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#    - Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
#    ou "Valor Inválido!", conforme o caso.

entrada = input('Digite o turno que voce estuda (M, V ou N): ')
turno = entrada.upper()
if turno != 'M' and turno != 'V' and turno != 'N':
    print('Turno invalido.')
else:
    if turno == 'M':
        mensagem = 'Bom Dia!'
    elif turno == 'V':
        mensagem = 'Boa Tarde!'
    else:
        mensagem = 'Boa Noite!'
    print(mensagem)