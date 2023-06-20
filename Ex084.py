# Crie uma classe chamada Cachorro que possua os
# atributos nome e raca. Crie um método chamado latir que
# exiba na tela a mensagem "O cachorro está latindo!".
# Em seguida, crie um objeto dessa classe e chame o método latir.

class cachorro:
    nome = None
    raca = None
    def __init__(self,nome,raca):
        cachorro.raca = raca
        cachorro.nome = nome

def latir(nome,raca):
    return print(f'O cachorro {nome}, da raça {raca} está latindo!')


nome = input('Digite o nome do cachorro: ')
raca = input('Digite a raça do cachorro: ')
cachorro1 = cachorro(nome,raca)
escolha = int(input('Deseja latir (0-Nao | 1-Sim): '))
if escolha is 0:
    print('FIM')
else:
    latir(nome,raca)

