#Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
print ("-=-=-"*20)

salario = float (input("--> Qual é o sálario do funcionario ? R$"))
novo = salario + (salario * 15 / 100)

print (f"--> Um funcionario que ganhava {salario:.2f} teve um aumento de 15% e passará a receber {novo:.2f}")

print ("-=-=-"*20)