cont = 0
soma = 0

for x in range(6):
	num = float(input())
	if(num >= 0):
		cont += 1
		soma += num

print("%d valores positivos" %cont)
print("%.1f" %(soma/cont))