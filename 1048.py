salario = float(input())
taxa = 0

if(salario >= 0 and salario <= 400.00):
	taxa = 0.15
elif(salario >= 400.01 and salario <= 800.00):
	taxa = 0.12
elif(salario >= 800.01 and salario <= 1200.00):
	taxa = 0.10
elif(salario >= 1200.01 and salario <= 2000.00):
	taxa = 0.07
elif(salario >= 2000.01):
	taxa = 0.04

per = taxa * 100
per = int(per)

print("Novo salario: %.2f" %(salario*(1+taxa)))
print("Reajuste ganho: %.2f" %(salario*(taxa)))
print("Em percentual: " + str(per) + " %")