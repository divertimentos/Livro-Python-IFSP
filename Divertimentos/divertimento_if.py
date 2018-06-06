nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))

#Nunca posso me esquecer do pemdas, senão o cálculo da média não fica correto.
media_notas = (nota1 + nota2) / 2

if media_notas >= 6:
    print("Sua nota é: %s." %media_notas)
    print("Você foi Aprovado")
elif media_notas >= 4:
    print("Seu status é: Exame!")
else:
    print("Sua nota é: %s." %media_notas)
    print("Você foi reprovado")
