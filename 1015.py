linha1 = input().split(" ")
linha2 = input().split(" ")

x1, y1 = linha1
x2, y2 = linha2

distancia = ((( float(x2)-float(x1) )**2)+(( float(y2)-float(y1) )**2)) ** 0.5

print("%.4f" %distancia)