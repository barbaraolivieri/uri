linha = input().split(" ")

duracao = 0
duracao2 = 0


h1, m1, h2, m2 = linha
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

inicio = (h1*60) + m1
final = (h2*60) + m2

if(h1 <= h2):
	duracao = final - inicio
	if(duracao == 0):
		print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(24,duracao%60))
	else:
		print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %((duracao-duracao%60)/60, duracao%60))

else:
	duracao = (24*60-inicio) + final
	print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %((duracao-duracao%60)/60, duracao%60))


