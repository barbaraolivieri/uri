linha = input().split(" ")

A, B, C = linha

A = float(A)
B = float(B)
C = float(C)

print("TRIANGULO: %.3f" %(A*C/2))
print("CIRCULO: %.3f" %(C*C*3.14159))
print("TRAPEZIO: %.3f" %(((A+B)*C)/2) )
print("QUADRADO: %.3f" %(B*B) )
print("RETANGULO: %.3f" %(A*B))
	