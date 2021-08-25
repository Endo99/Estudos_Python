vector = []

for i in range(0, 8):
    vector.append(int(input('Digite um número: \n')))


X = int(input('Digite um valor de 0 a 7: \n'))
Y = int(input('Digite outro valor de 0 a 7: \n'))
soma = vector[X] + vector[Y]

print(soma)