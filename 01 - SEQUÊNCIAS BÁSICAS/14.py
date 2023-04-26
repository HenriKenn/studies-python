#A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
print ("-=-=-"*20)
km = float(input ("--> Qual é a Kilometragem do veículos? "))

dias = int(input("--> Quanto dias o carro ficou alugado ? "))

pago = ( dias * 90 ) + (km * 0.20)

print (f"--> O valor do aluguél do veículo ficou R${pago:.2F}")

print ("-=-=-"*20)
