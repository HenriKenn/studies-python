#Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
#80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
#o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
print("-=-=-"*20)

velo = int(input("--> Qual velocidade do veículo? "))

velocidade_maxima = 80


if velo > 80:
    
    diferença =  velo - velocidade_maxima
    multa = diferença * 5
    print (f"--> Radar: Você foi multado por excesso de velocidade e foi multado em R${multa}")

else:

    print ("--> Radar: Você não foi multado, Parabéns! ")

print("-=-=-"*20)