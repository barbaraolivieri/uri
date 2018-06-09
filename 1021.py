x = float(input())

inteiro = x
x = 100 * x 
aux1 = x





print("NOTAS:")
print("%d nota(s) de R$ 100.00" %(inteiro/100))
aux = (inteiro%100)
print("%d nota(s) de R$ 50.00" %(aux/50) )
aux = (aux%50)
print("%d nota(s) de R$ 20.00" %(aux/20) )
aux = (aux%20)
print("%d nota(s) de R$ 10.00"  %(aux/10))
aux = (aux%10)
print("%d nota(s) de R$ 5.00" %(aux/5))
aux = (aux%5)
print("%d nota(s) de R$ 2.00"  %(aux/2))
aux = (aux%2)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %aux)
aux1 = aux1%100
print("%d moeda(s) de R$ 0.50" %(aux1/50) )
aux1 = aux1%50
print("%d moeda(s) de R$ 0.25" %(aux1/25) )
aux1 = aux1%25
print("%d moeda(s) de R$ 0.10" %(aux1/10) )
aux1 = aux1%10
print("%d moeda(s) de R$ 0.05" %(aux1/5) )
aux1 = aux1%5
print("%d moeda(s) de R$ 0.01" %(aux1/1) )
