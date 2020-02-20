import datetime

def dias_de_vida(dia,mes,ano):
    data1=datetime.date(year=ano,month=mes,day=dia)
    z=datetime.date.today()
    return (z-data1)

dia=int(input("Insira o dia do seu aniversário: "))
mes=int(input("Insira o mes do seu aniversário: "))
ano=int(input("Insira o ano do seu aniversário: "))
x=dias_de_vida(dia,mes,ano)

print("Você tem ", x," dias de vida")

