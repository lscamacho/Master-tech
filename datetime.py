import datetime as dt

dia_atual = dt.date(year=2019, mounth=2, day=20)

def c_dias_de_vida(data):

    hoje = datetime.date.today()

    dias_vida = hoje - data
    return dias_de_vida

retorno = c_dias_de_vida(dia_atual)

print(retorno)