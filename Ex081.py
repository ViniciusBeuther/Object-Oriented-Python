#LISTA 04
# Faça um programa com um menu, que permite escolher
# qual das funcoes acima sera executada
def produto(a, b, c):
    produto = a * b * c
    return (produto)

def fatorial(a):
    fatorial = 1
    while a > 0:
        fatorial = fatorial * a
        a -= 1
    return fatorial

def media(notas):
    soma = 0
    for e in notas:
        soma += e
    return soma / len(notas)


def mediaPeso(notas, peso):
    soma = 0
    somaNotas = 0
    i = 0
    while i < len(notas):
        soma += (notas[i] * (peso[i]))
        somaNotas += peso[i]
        i += 1
    return (soma / somaNotas)

def calculaPreco(preco, percentual):
    valorDesconto = preco * (percentual / 100)
    return (preco - valorDesconto)

def maximo(lista):
    maior = lista[0]
    for e in lista:
        if e > maior:
            maior = e
    return maior

def inverte(lista, qtd):
    inversa = []
    quantidadeNumeros = len(lista)
    for e in lista[::-1]:
        inversa.append(e)
    return inversa

def mediaString(soma, i):
    return soma / i

def procurar(lista, nome):
    status = 'False'
    for e in lista:
        if e == nome:
            status = 'True'
            break
        else:
            status = 'False'
    return status

while True:

    print('\n\n-----FUNCOES-----')
    print('1- 3 Argumentos')
    print('2- Fatorial')
    print('3- Media 4 notas')
    print('4- Media 4 notas com peso')
    print('5- Preço final de produto')
    print('6- Valor maximo de uma L[]')
    print('7- Inversor de Lista')
    print('8- Calcula média de numeros')
    print('9- Buscador de nomes')
    print('0- Encerrar')

    escolha = int(input('\nDigite a opção desejada: '))
    if escolha == 0:
        print('FIM!')
        break
    elif escolha == 1:
        a = int(input('Digite o valor A: '))
        b = int(input('Digite o valor B: '))
        c = int(input('Digite o valor C: '))
        print(f'O produto dos elementos é {produto(a, b, c):.2f}')

    elif escolha == 2:
        a = int(input('Digite um numero inteiro: '))
        print(f'Fatorial é {fatorial(a)}')

    elif escolha == 3:
        notas = []
        i = 0
        while i < 4:
            notas.append(float(input(f'Digite a nota {i + 1}: ')))
            i += 1
        print(f'A média das notas digitadas é {media(notas):.2f}')

    elif escolha == 4:
        peso = []
        notas = []
        i = 0
        while i < 4:
            notas.append(float(input(f'Digite a nota {i + 1}: ')))
            peso.append(float(input(f'Digite o peso {i + 1}: ')))
            i += 1
        print(f'A média foi de {mediaPeso(notas, peso)}')

    elif escolha == 5:
        preco = float(input('Digite o preco do produto: R$ '))
        percentual = float(input('Quantos % de desconto: '))
        print(f'O valor final do produto é: R$ {calculaPreco(preco, percentual):.2f}')

    elif escolha == 6:
        L = [1, 2, 3, 4, 5, 6, 11, 25, 67, 98, 20]
        print(f'O maior valor da lista é {maximo(L)}')

    elif escolha == 7:
        i = 0
        L = []
        while True:
            L.append(int(input('Digite um numero: ')))
            i += 1
            parar = int(input('Continuar 1-Sim 0-Nao: '))
            if parar is 0:
                break
        print(f'O valor invertido {inverte(L, i)}')

    elif escolha == 8:
        i = 0
        L = []
        soma = 0
        while True:
            number = input('Digite um numero ou "Fim" para encerrar: ')
            if number.isdigit() == True:
                i += 1
                aux = float(number)
                soma += aux
            else:
                if number.upper() == 'FIM':
                    break
        print(f'A media dos valores digitados é {mediaString(soma, i)}')

    elif escolha == 9:
        L = []
        while True:
            nomes = input('Digite um  (0-Encerra): ')
            if nomes == '0':
                break
            L.append(nomes)

        nome = input('Digite o nome que deseja procurar: ')
        print(f'\n{procurar(L, nome)}')



