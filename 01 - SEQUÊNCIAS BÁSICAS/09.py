#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

print ("-=-=-"*20)
reais = float (input("--> Digite quanto você tem em R$ na sua carteira: "))

dolar = (reais/5.06)

print (f"--> Com R${reais} Você pode comprar U${dolar:.2f}.")
print ("-=-=-"*20)