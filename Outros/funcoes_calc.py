#Função de percentagem:

def percentagem(lido = input, total = input, multiplica = 100):
    resultado_porcentagem = lido / total * multiplica
    return resultado_porcentagem

#Função de adição

def plus(parcela1 = input, parcela2 = input):
    resultado_soma = parcela1 + parcela2
    return resultado_soma

#Calculadora de percentagem:

total = input("Total de páginas \n")
lido = input("Páginas lidas \n")

resposta_porcentagem = percentagem(int(lido), int(total)) #lido / total * 100

print(resposta_porcentagem)

#Calculadora de adição

parcela1 = input("Insira a parcela 1 \n")
parcela2 = input("Insira a parcela 2 \n")

resposta_soma = plus(int(parcela1), int(parcela2))
print(resposta_soma)
