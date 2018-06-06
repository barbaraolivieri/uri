n = int(input())

horas = int(n/(60*60))
n = n % (60*60)
minutos = int(n/60)
segundos = int(n % 60)

print(repr(horas)+":"+repr(minutos)+":"+repr(segundos))