from pycep import PyCep
print('---LEITOR DE CEP---')
cepUser = input('Digite o seu CEP: ')
cep1 = PyCep(cepUser)

if len(cepUser) < 8 or len(cepUser) > 8:
    print('O CEP digitado é inválido!')
else:
    #Apresentando dados
    print(f'Você mora na cidade de {cep1.dadosCep["localidade"]} em {cep1.dadosCep["uf"]}')
    print(f'No bairro {cep1.dadosCep["bairro"]} na {cep1.dadosCep["logradouro"]}')
