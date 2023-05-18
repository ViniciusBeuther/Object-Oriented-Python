#LISTA4 - FUNCOES
# 5) Faça uma funcao chamada calculaPreco, que recebe 2 parametros
# valor de compra e desconto em %. retornar o valor final do produto

def calculaPreco(preco,percentual):
    valorDesconto = preco * (percentual/100)
    return (preco-valorDesconto)

preco = float(input('Digite o preco do produto: R$ '))
percentual = float(input('Quantos % de desconto: '))

print(f'O valor final do produto é: R$ {calculaPreco(preco,percentual):.2f}')