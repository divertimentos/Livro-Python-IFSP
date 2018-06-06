#Escrever um programa que leia um número de 0 a 10 e mostre a tabuada desse número.

entrada = int(input("Descubra a tabuada de um número: \n"))
multiplicador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = 1

for item in multiplicador:
    tabuada = entrada * item
    print("Resultado: %s" %tabuada)

#Achei que poderia ter ficado menos roots, mas printou o resultado que eu queria usando o for.
