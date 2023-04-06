#Imprimir os 10 primeiros multiplos de 3
from time import sleep
x = 0
while x <= 30:
    if x % 3 == 0:
        print(x)
        sleep(1)
    x+=1
