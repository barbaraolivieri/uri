linha = input().split(" ")
duracao = 0

A, B = linha
A = int(A)
B = int(B)

if(B > A):
	duracao = B - A
elif (B == A):
	duracao = 24
else:
	duracao = 24 - A
	duracao = duracao + B

print("O JOGO DUROU %d HORA(S)" %duracao)