numero = int(input("Qual a tabuada quer saber? Digite um numero de 1 a 10: "))

print(" Tabuada do ",numero,":\n")
for x in range(1, 11):
    print(numero," X ",x," = ",numero*x, "\n")