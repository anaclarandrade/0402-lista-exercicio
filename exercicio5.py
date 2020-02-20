import math
x=float(input("Insira o valor do raio: "))
def area(x):
    y=round((math.pi * x * x),2)
    return y
print ("A area é ",area(x))
def comprimento(x):
    z=round((math.pi * x * 2),2)
    return z
print ("O comprimento é ",comprimento(x))