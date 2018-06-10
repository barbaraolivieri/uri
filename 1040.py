linha = input().split(" ")

N1, N2, N3, N4 = linha
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

nota_exame = 0.0
media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

if media >= 7.0:
	print("Media: %.1f" %media)
	print("Aluno aprovado.")
elif media >= 5.0 and media <= 6.9:
	print("Media: %.1f" %media)
	print("Aluno em exame.")
	exame = float(input())
	print("Nota do exame: %.1f" %exame)
	media2 = (media + exame) / 2
	if media2 >= 5.0:
		print("Aluno aprovado.")
		print("Media final: %.1f" %media2)
	else:
		print("Aluno reprovado.")
		print("Media final: %.1f" %media2)
else:
	print("Media: %.1f" %media)
	print("Aluno reprovado.")