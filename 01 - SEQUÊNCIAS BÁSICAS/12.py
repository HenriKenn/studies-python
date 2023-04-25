#Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

print("-=-=-"*20)
preço = float (input("--> Digite o preço do produto: R$"))

novo = preço - (preço * 5 / 100)

print(f"--> O produto que custava R${preço:.2f} está com promoção de 5% e passará a custa apenas R${novo:.2f}")

print("-=-=-"*20)