#Digitar um CPF e valida-lo
from cpf_generator import CPF
cpf = input('Digite seu CPF: ')

if CPF.validate(cpf) == True:
    print(f"O CPF {CPF.format(cpf)} é Válido!")
else:
    print(f"O CPF {CPF.format(cpf)} Inválido!")