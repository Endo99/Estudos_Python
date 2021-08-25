v = []

for i in range(0, 10):
    v.append(int(input(f'Insira um número para o vetor {i+1}: \n')))

v1 = []
v2 = []

for i in range(len(v)):
    if i % 2 == 0:
        v2.append(v[i])
    else:
        v1.append(v[i])

print(f'Os elementos Utilizados de v1 é: {v1}')
print(f'Os elementos Utilizados de v2 é: {v2}')
