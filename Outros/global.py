#Variável global:

def soma(x, y):
    global total
    total = x+y
    print("Total soma = ", soma)

#Programa principal

global total
total = 10
soma(3, 5)
print("Total principal = ",total)

#Não deu certo essa porra.
