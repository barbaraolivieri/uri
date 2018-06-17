maior = 0
pos = 0

for x in range(100):
	n = int(input())
	if n > maior:
		maior = n
		pos = x


print(maior)
print("%d" %(pos+1))