#7) Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhecer, engordar, crescer. Obs: Por padrão, a cada ano quea pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm ao ano. A pessoa engorda 0,5 kg por ano.
# Faça uma projeção para X anos, informando o novo peso e/ou altura.

class pessoa:
    __nome = None
    __idade = None
    __peso = None
    __altura = None

    def __init__(self,nome,idade,peso,altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def getInfo(self):
        return (print(f'nome: {nome}\nidade: {idade} anos\npeso: {peso} kg\naltura: {altura} m'))

    def envelhecer(self, peso, idade, altura):
        if idade < 21:
            self.__peso += 0.5
            self.__altura += 0.05

    def projecao(self, numeroDeAnos, peso, idade, altura):
        i = 0
        while i < numeroDeAnos:
            if idade < 21:
                peso +=0.5
                altura += 0.05
        return self.__idade, self.__peso, self.__altura


pessoa1 = pessoa()
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
infoProjecao = int(input('Digite quantos anos no futuro deseja ver: '))
pessoa1.getInfo()
print(pessoa1.projecao(infoProjecao, peso, idade, altura))


