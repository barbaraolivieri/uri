i = 1
j = 7
cont = 7

while i <= 9:
	for x in range(3):
		print("I=%d J=%d" %(i,j))
		j -= 1
	i += 2
	cont += 2
	j = cont