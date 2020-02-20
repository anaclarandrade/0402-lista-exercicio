def somar(x,y):
    z=x+y
    if z < 40:
        return ("Ops, só retorno valores até maiores que 40")
    else:
        return z

soma=somar(40,1)
print(soma)