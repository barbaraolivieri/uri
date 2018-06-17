n = int(input())
c = 0
r = 0
s = 0


for x in range(n):
	linha = input().split(" ")
	a, b = linha
	a = int(a)
	if(b == 'C'):
		c += a
	elif(b == 'R'):
		r += a
	else:
		s += a

total = c+r+s
print("Total: %d cobaias" %total)
print("Total de coelhos: %d" %c)
print("Total de ratos: %d" %r)
print("Total de sapos: %d" %s)


print("Percentual de coelhos: %.2f" %((100*c)/total), '%')
print("Percentual de ratos: %.2f" %((100*r)/total), '%')
print("Percentual de sapos: %.2f" %((100*s)/total), '%')