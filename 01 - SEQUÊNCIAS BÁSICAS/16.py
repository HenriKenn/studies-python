# [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
# fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
# já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
# quantos dias de vida um fumante perderá e exiba o total em dias.

print("-=-="*20)

cigarros_por_dia = int(input("--> Quantidade de cigarros por dia: "))
anos_fumando = int(input("--> Quantidade de anos fumando: "))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
redução_em_dias = redução_em_minutos / (24 * 60)

print(f"--> Redução do tempo de vida em dias: {redução_em_dias:.0f}")

print("-=-="*20)
