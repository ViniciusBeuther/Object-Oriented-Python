#calcule a área, em cm², de um triângulo retângulo,
# recebendo a base e a altura. exiba o reusultado na tela

h = float(input('Digite a Altura do triangulo em cm: '))
b = float(input('Agora, digite a Base do triangulo em cm: '))

if h < 0 or b < 0:
    print('Valores negativos!')
else:
    print(f'O valor da area do triangulo é de {(b*h)/2} cm^2')