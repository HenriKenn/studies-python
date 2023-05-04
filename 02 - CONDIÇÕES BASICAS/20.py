# Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

print("-=-="*20)

numb = float(input("--> Digite um número para saber se é par ou impar: "))

result = (numb % 2)

if result == 0:
    print(f"--> O número é par.")

else:

    print(f"--> O número é impar.")

print("-=-="*20)