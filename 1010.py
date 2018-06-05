A = input().split(" ")
B = input().split(" ")

C1, N1, P1 = A
C2, N2, P2 = B

preco =(int(N1)*float(P1)) + (int(N2)*float(P2)) 

print("VALOR A PAGAR: R$ %.2f" %preco )