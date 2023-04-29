#Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
print ("-=-=-"*20)
ano = int(input("--> Digite seu ano de nascimento: "))

idade = (2023 - ano)

print (f"--> Sua idade é {idade}anos.")

if idade < 65:
    print("--> Você precisa votar. Obrigatorio !!!")

else:
    print("--> Você não é mais obrigado votar.")

print ("-=-=-"*20)
