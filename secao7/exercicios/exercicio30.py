v1 = []
v2 = []

for i in range(1, 11): #1, 11
    v1.append(int(input(f'Insira um número para o vetor 1, número {i}: \n')))
    v2.append(int(input(f'Insira um número para o vetor 2, número {i}: \n')))

intersection = []

numeros = {}

for i in range(len(v1)):
    numeros[i] = v1[i]

print(numeros)

for i in range(len(v1)):
    for j in range(len(v2)):
        if v1[i] == v2[j]:
            intersection.append(v1[i])

print(f'Os números iguais são {intersection}')