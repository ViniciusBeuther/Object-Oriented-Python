#Mostrar quantas vogais há na frase
frase = input("Digite uma frase: ")
vogais = "aAeEiIoOuU"
contadorVogais = 0
i = 0

while i < len(frase):
    if frase[i] in vogais:
        contadorVogais += 1
    i += 1

print(f"A frase digitada contém {format(contadorVogais)} vogais.")
