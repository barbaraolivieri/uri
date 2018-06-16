n = int(input())

for x in range(n):
	y = int(input())
	if(y == 0):
		print("NULL")
	elif (y % 2 == 0):
		if(y > 0):
			print("EVEN POSITIVE")
		else:
			print("EVEN NEGATIVE")
	else:
		if(y > 0):
			print("ODD POSITIVE")
		else:
			print("ODD NEGATIVE")