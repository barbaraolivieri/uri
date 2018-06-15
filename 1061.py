inicio = input().split(" ")
linha1 = input().split(" : ")
final = input().split(" ")
linha2 = input().split(" : ")

dia, x = inicio
h1, m1, s1 = linha1
dia2, y = final
h2, m2, s2 = linha2

x = int(x)
y = int(y)
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)
h2 = int(h2)
m2 = int(m2)
s2 = int(s2)


long  int dur = (y*86400 + h2*3600 + m2*60 + s2) - (x*86400 + h1*3600 + m1*60 +s1) 

dias = dur/86400
horas = (dur%86400)/3600
minutos =((dur%86400)%3600)/60
segundos = (((dur%86400)%3600)%60)

print("%d dia(s)" %dias)
print("%d horas(s)" %horas )
print("%d minuto(s)" %minutos )
print("%d segundo(s)" %segundos )