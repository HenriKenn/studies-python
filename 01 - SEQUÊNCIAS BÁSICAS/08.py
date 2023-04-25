# Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

print ("-=-"*20)
metros = float(input("Digite a distância em metros: "))

km = (metros / 1000)
hm = (metros / 100)

cm = (metros * 100)
mm = (metros * 1000)

dm = (metros * 10)
dam = (metros / 10)

print(f"A distância de {metros}m corresponde a:")

print(f"{km} km\n {hm} hm \n {dam} dam \n {dm} dm \n {cm} cm \n {mm} mm")
print ("-=-"*20)