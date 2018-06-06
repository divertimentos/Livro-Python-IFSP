#Escrever um programa de soma:

lista_numeros = list(range(3, 334, 3))
soma = 0

for numero in lista_numeros:
    soma = soma + numero
print(soma)

#Escrever um programa que leia 10 notas e retorne a média.

lista_notas = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
soma = 0
for numero in lista_notas:
    soma = soma + numero
media = soma / len(lista_notas)
print("A média é %s:" %media)
