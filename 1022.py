linha = input().split(" ")

A, B, C, D = linha
A = int(A)
B = int(B)
C = int(C)
D = int(D)
zero = 0


if (B > C) & (D > A) & (C+D > A+B) & (C > zero) & (D > zero) & (A % 2 == zero):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")