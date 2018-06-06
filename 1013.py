linha = input().split(" ")

A, B, C = linha
A = int(A)
B = int(B)
C = int(C)


x = ((A+B+abs(A-B))/2)

maior =  ((C+x+abs(C-x))/2)

print("%d eh o maior" %maior)