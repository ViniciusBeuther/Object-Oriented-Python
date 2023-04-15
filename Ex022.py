quantidade = int(input('Digite a quantidade de primos: '))
contador = 3
divisor_impar = 3
fim = 0

while fim < quantidade:
    while True:
        if contador == divisor_impar:
            print(contador)
            contador +=2
            fim+=1
            divisor_impar = 3
            break
        elif contador % divisor_impar != 0:
            divisor_impar += 2
            break
        elif contador % divisor_impar == 0:
            contador+=2
            break
