tipo = input()
animal = input()
comida = input()

if tipo == "vertebrado":
	if animal == "ave":
		if comida == "carnivoro":
			resp = "aguia"
		else:
			resp = "pomba"
	else:
		if comida == "onivoro":
			resp = "homem"
		else:
			resp = "vaca"
else:
	if animal == "inseto":
		if(comida == "hematofago"):
			resp = "pulga"
		else:
			resp = "lagarta"
	else:
		if(comida == "hematofago"):
			resp = "sanguessuga"
		else:
			resp = "minhoca"

print(resp)
