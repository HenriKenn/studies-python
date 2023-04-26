#Desenvolvido por Prô Terra - MakerZine
#Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.

print("-=-=-"*20)
def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta == 0:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta = 0, temos um único valor de raiz (X1 = x2): ",x1)
  elif delta > 0:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta > 0, temos dois valores distintos de raízes: ",x1,"e",x2)
  else:
    print()
    print("Nossa equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta < 0, não temos raízes reais!")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
bhaskara(a,b,c)
print("-=-=-"*20)