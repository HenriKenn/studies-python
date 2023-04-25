# Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

print("-=-=-"*20)
larg = float(input("--> Digite a largura da parede: "))
altu = float(input("--> Digite a altura da parede: "))

area = larg * altu

print(f"--> Sua parede tem dimensão de {larg}x{altu} e sua áraa é de {area}m².")

tinta = area / 2

print(f"--> Para pintar está parede, você precisará de {tinta}Litros de tinta.")

print("-=-=-"*20)
