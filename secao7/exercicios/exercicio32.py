x = []
y = []

while len(x) < 5:

    numero = int(input(f'Insira um número {len(x) + 1}: \n'))

    if numero not in x:
        x.append(numero)

while len(y) < 5:

    numero = int(input(f'Insira um número {len(y) + 1}: \n'))

    if numero not in y:
        y.append(numero)


for i in range(len(x)):
    for j in range(len(y)):
        if x.index(x[i]) == y.index(y[j]):
            soma = x[i] + y[j]
            print(soma, end=" ")
