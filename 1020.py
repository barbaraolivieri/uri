dias = int(input())

ano = int(dias / 365)
dias = dias - (ano*365)
mes = int(dias/30)
dias = dias - (mes * 30)



print("%d ano(s)" %ano)
print("%d mes(es)" %mes)
print("%d dia(s)" %dias)