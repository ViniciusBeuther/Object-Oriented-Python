# ENCAPSULAMENTO
#slide 10 - 6)
from math import ceil

class retangulo:
    comprimento = None
    largura = None

    def __init__(self):
        self.comprimento = 0
        self.largura = 0

    def setComprimento(self, valorComprimento):
        comprimento = valorComprimento

    def setLargura(self,valorLargura):
        largura = valorLargura

    def calcularArea(self,largura,valorComprimento):
        area = largura * valorComprimento
        return area

    def calcularPisos(self,area):
        pisos = area
        return pisos

    def calcularRodape(self,largura,comprimento):
        rodape = (largura * 2) + (comprimento * 2)
        rodape = ceil(rodape)
        return rodape


comodo = retangulo()
largura = float(input('Digite a largura do cômodo (m): '))
comprimento = float(input('Digite o comprimento do cômodo (m): '))
print(f'Area: {comodo.calcularArea(largura,comprimento)} m2')
print(f'Rodapes necessarios (1m): {comodo.calcularRodape(largura,comprimento)}')
print(f'Pisos necessarios (1m x 1m): {comodo.calcularPisos(comodo.calcularArea(largura,comprimento))}')
