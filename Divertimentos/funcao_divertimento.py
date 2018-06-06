#Criar uma função para desenhar uma linha, usando o caractere '_'. O tamanho da linha deve ser definido na chamada da função.



#Criar uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista enumerando-os.

lista = ["Um", "Dois", "Três", "Quatro", "Cinco"]
def enumerar(lista):
    return lista

contador = 0
for i in lista:
    contador += 1
    print("Resultado: %s" %contador, "-", i)
#CONSEGUI


#Criar uma função que receba como parâmetro uma lista com valores numéricos e retorne a média desses valores.

lista_numeros = [1, 2, 3, 4, 5]
counter = 0

def media(lista_numeros):
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    print(media)
media(lista_numeros)
