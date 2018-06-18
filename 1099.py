n = int(input())

for t in range(n):
	linha = input().split(" ")
	soma = 0
	x, y = linha
	x = int(x)
	y = int(y)
	if(x>y):
		a = x
		x = y
		y = a
	for i in range(x+1,y):
		if(i % 2 != 0):
			soma += i
	print(soma)