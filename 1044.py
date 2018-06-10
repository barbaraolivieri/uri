linha = input().split()
linha = list(map(int,linha))

A, B = linha

if (B%A == 0) or (A%B == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')