linha = input().split(" ")

x, Y = linha
x = int(x)
Y = int(Y)

if x == 1:
	print("Total: R$ %.2f" %(4.00*Y))
elif x == 2:
	print("Total: R$ %.2f" %(4.50*Y))
elif x == 3:
	print("Total: R$ %.2f" %(5.00*Y))
elif x == 4:
	print("Total: R$ %.2f" %(2.00*Y))
elif x == 5:
	print("Total: R$ %.2f" %(1.50*Y))