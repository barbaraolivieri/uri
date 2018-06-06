x = int(input())

res = x

cem = int(x/100)
x = x % 100
cinquenta = int(x/50)
x = x % 50
vinte = int(x/20)
x = x % 20
dez = int(x/10)
x = x % 10
cinco = int(x/5)
x = x % 5
dois = int(x/2)
x = x % 2

print(res)
print("%d nota(s) de R$ 100,00" %cem)
print("%d nota(s) de R$ 50,00" %cinquenta)
print("%d nota(s) de R$ 20,00" %vinte)
print("%d nota(s) de R$ 10,00" %dez)
print("%d nota(s) de R$ 5,00" %cinco)
print("%d nota(s) de R$ 2,00" %dois)
print("%d nota(s) de R$ 1,00" %x)


