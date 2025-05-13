nota_prova = float(input("Digite sua nota da prova: "))
nota_trabalho = float(input("Digite sua nota do trabalho: "))
media = (nota_prova + nota_trabalho) /2
print (f"Sua média é: {media}")
if media >= 7:
    print ("Aprovado!")
else:
    print ("Reprovado!")
    
