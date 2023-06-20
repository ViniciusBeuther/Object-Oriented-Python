# ENCAPSULAMENTO
# Crie uma classe que modele uma bola
# Atributo: cor, circunferencia e material | metodos:TrocaCor e MostraCor

class bola:
    __cor = None
    __circunferencia = None
    __material = None

    def __init__(self):
        self.__cor = 'Transparente'
        self.__circunferencia = 5
        self.__material = 'Borracha'

    def getColor(self):
        return self.__cor

    def setColor(self,colorToSet):
        self.__cor = colorToSet
        return print('Cor definida.')

bola1 = bola()
print(bola1.getColor())
cor1 = input('Digite a cor: ')
bola1.setColor(cor1)
print(bola1.getColor())