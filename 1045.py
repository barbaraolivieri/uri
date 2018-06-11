linha = input().split(" ")
linha = list(map(float,linha))

A,B,C = sorted(linha)[::-1]

flag = True

if(A >= B+C):
	print("NAO FORMA TRIANGULO")
	flag = False

if ((A**2 == (B**2)+(C**2)) and flag):
	print("TRIANGULO RETANGULO")
elif ((A**2 > (B**2)+(C**2)) and flag):
	print("TRIANGULO OBTUSANGULO")
elif ((A**2 < (B**2)+(C**2)) and flag):
	print("TRIANGULO ACUTANGULO")

if(A == B and B == C and flag):
	print("TRIANGULO EQUILATERO")
elif((A == B or B == C) and (A != B or B != C) and flag):
	print("TRIANGULO ISOSCELES")
