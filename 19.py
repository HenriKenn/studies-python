#Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
#não um bom aproveitamento (se ficou acima da média 7.0).

print("-=-="*20)
nome = str(input("--> Qual é o seu nome ? "))
numb = float(input("--> Digite a primeira nota do aluno: "))
numb2 = float(input("--> Digite a segunda nota do aluno: "))

result = (numb + numb2)/2

print(f"--> Sua média foi de {result}")

if result > 7.0:

    print("--> Parabéns você passou !")

else:

    print("--> Infelismente você foi reprovado !")

print("-=-="*20)