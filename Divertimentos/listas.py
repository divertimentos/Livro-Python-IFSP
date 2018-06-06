#Propriedades das listas:

L = [3, 'abacate', 9.7, [5, 6, 3], "Python", (3,'j')]
print(L[2])
print(L[3])
print(L[3][1])

L[3] = "Morango"
print(L)

#Concatenação:

a = [0, 1, 2]
b = [3, 4, 5]
c = a + b
print(c)

#Repetição:

A = [1, 2]
B = [L * 4]
print(B)

#Fatiamento:

print(L[1:4])
print(L[2:])
print(L[:4])
