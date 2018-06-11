linha = input().split()
linha = list(map(float,linha))

A, B, C = linha

if(A+B > C and B+C > A and A+C > B ):
    print("Perimetro = %.1f" %(A+B+C))
else:
    print("Area = %.1f" %(0.5*(A+B)*C))