vetor = []

for i in range(0, 10):
    valor = int(input('Insira um valor: \n'))
    if valor < 0:
        vetor.insert(i, 0)
    else:
        vetor.insert(i, valor)

print(f'{vetor}')