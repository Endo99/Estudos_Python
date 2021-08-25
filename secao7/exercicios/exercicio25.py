vetor = []

numero = ''
for i in range(0, 100):
    numero = str(i)
    if i % 7 == 0 or numero[len(numero)-1] == '7':
        vetor.append(i)
print(vetor)