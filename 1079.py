n = int(input())

for x in range(n):
	linha = input().split(" ")
	a,b,c = linha
	a = float(a)
	b = float(b)
	c = float(c)
	media = float(((2*a)+(3*b)+(5*c))/10.0)
	print("%.1f" %media)
