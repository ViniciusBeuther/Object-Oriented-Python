# EX2 SLIDE-9
# Altere o exercício anterior para criar uma lista de objetos do tipo Pessoa, defina seus atributos e imprima os mesmos na
# tela.

class pessoa:
    nome = None
    idade = None
    cpf = None
    def __init__(self, nome, idade, cpf):
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.cpf = cpf
lista = []
pessoa1 = pessoa('Vinicius', '20 Anos', '123.456.789-00')
lista.append(pessoa1.nome)
lista.append(pessoa1.cpf)
lista.append(pessoa1.idade)
print(lista)

