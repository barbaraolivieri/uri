i = float(0)
j = float(1)
cont = 0
flag = 0

while i <= 2:
	for x in range(3):
		if(i == 0 or i == 1 or i == 2.00 or flag == 0):
			print("I=%.0f J=%.0f" %(i,j))
		else:
			print("I=%.1f J=%.1f" %(i,j))
		j += 1
	i += 0.2
	cont+=1
	j = cont + 0.2
	flag = 1
