vetor = []

for i in range(0, 5):
    vetor.append(float(input('Insira um valor: \n')))

code = int(input('Digite um código: \n'))

if code == 0:
    print('Programa encerrado!')
elif code == 1:
    print(vetor)
elif code == 2:
    print(vetor[::-1])
else:
    print('O código {code} digitado, não é válido!')