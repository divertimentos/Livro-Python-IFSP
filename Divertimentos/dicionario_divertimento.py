lanchonete = {
"Salgado": 4.50,
"Lanche": 6.50,
"Suco": 3.00,
"Refrigerante": 3.50,
"Doce": 1.00
}

#Dicionário com nomes de 5 alunos. Calcular a média de notas da turma.

alunos = {
"Amanda": 9.0,
"Luiza": 8.0,
"Pedro": 7.0,
"Poliane": 6.0,
"Guilherme": 5.0
}
print("Lista de alunos e notas: %s" %alunos)

#filtro somente as notas e atribuo à variável "notas":
notas = alunos.values()
#somo os valores das notas dentro da variável "notas" e atribuo o resultado a "soma_notas":
soma_notas = (sum(notas))
#calculo o número de notas/alunos e atribuo-o à variável "indice":
indice = (len(alunos.values()))
#calculo a média e atribuo o resultado a "media_notas":
media_notas = soma_notas / indice
#printo o resultado:
print("A média de notas da turma é: %s." %media_notas)
