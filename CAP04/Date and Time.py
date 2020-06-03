import datetime

agora = datetime.datetime.now()
print(agora)

#Criando a data
t = datetime.time(17, 36, 28)
print(t)

print("Hora:", t.hour)
print("Minuto:", t.minute)
print("Segundo:", t.second)

hoje = datetime.date.today()
print("A data de hoje é", hoje)
print("ctime:", hoje.ctime())
print("Ano:", hoje.year)
print("Mês:", hoje.month)
print("Dia:", hoje.day)

"Calculo da data!!!"
d1 = datetime.date(2020, 6, 3)
print(d1)
d2 = datetime.date(2015, 5, 31)
print(d2)

#Diferença entre duas datas
print(d1-d2)
