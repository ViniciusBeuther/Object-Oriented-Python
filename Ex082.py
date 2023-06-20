# Orientação a objetos com python

class TV:
    ligada = None #Definindo atributos
    canal = None #Definindo atributos
    tamanho = None
    marca = None
    def __init__(self): #método construtor, criando padrão do obj
        self.ligada = False
        self.canal = canal
##################################################################
tvSala = TV() #criando a tvNumero1 e dizendo que é um objeto do tipo TV
tvQuarto = TV()

#Definindo atributos da tvSala
tvSala.ligada = True
tvSala.canal = 1
tvSala.tamanho = 48
tvSala.marca = 'Samsung'

#Definindo atributos da tvQuarto
tvQuarto.ligada = False
tvQuarto.canal = 2
tvQuarto.tamanho = 32
tvQuarto.marca = 'LG'

print('---TV DA SALA---')
print(f'Tv ligada: {tvSala.ligada}')
print(f'Canal: {tvSala.canal}')
print(f'Marca: {tvSala.marca}')
print(f'Tamanho: {tvSala.tamanho} polegadas')

print('---TV DO QUARTO---')
print(f'Tv ligada: {tvQuarto.ligada}')
print(f'Canal: {tvQuarto.canal}')
print(f'Marca: {tvQuarto.marca}')
print(f'Tamanho: {tvQuarto.tamanho} polegadas')