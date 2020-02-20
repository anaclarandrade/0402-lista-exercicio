import math

def circulo(x):
    if x.isnumeric()==True:
        area=round(float(x)**2*math.pi,2)
        comprimento= round(float(x)*2*math.pi,2)
        texto = ("A área é " + str(area)+ " e o comprimento é "+str(comprimento)+".")
        return texto
    else:
        return ("Insira um número")
x=input("Insira o valor do raio: ")
z= circulo(x)
print (z)


