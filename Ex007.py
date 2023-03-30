# Entrar com gasto mensal KW e setor do imovel (Residencial, Comercial ou Industrial) e calcular o preço da conta
consumoKW = int(input('Qual o seu consumo (KWh): '))
if consumoKW > 0:
    tipo = input('Qual o tipo da sua intalação (I-Industrial | R-Residencial | C-Comercial): ')
    if tipo == 'R' or tipo == 'r' or tipo == 'C' or tipo == 'c' or tipo == 'I' or tipo == 'i':
        if tipo == 'R' or tipo == 'r':
            instalacao = 'Residencial'
            if consumoKW <= 500:
                valorConta = 0.4 * consumoKW
            else:
                valorConta = 0.65 * consumoKW
        elif tipo == 'C' or tipo == 'c':
            instalacao = 'Comercial'
            if consumoKW <= 1000:
                valorConta = 0.55 * consumoKW
            else:
                valorConta = 0.60 * consumoKW
        elif tipo == 'I' or tipo == 'i':
            instalacao = 'Industrial'
            if consumoKW <= 5000:
                valorConta = 0.55 * consumoKW
            else:
                valorConta = 0.60 * consumoKW
        print(f'Para o tipo de instalação {instalacao:} o consumo de {consumoKW:} KW/h tera um valor na conta de R$ {valorConta:.2f}')
    else:
        print('Informação INVÁLIDA!')
else:
    print('Informação INVÁLIDA!')