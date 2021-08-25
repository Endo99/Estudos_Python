vetorA = [int(input(f'Insira um número para o vetor A {i+1}: \n')) for i in range(0, 10)]
vetorB = [int(input(f'Insira um número para o vetor B {i+1}: \n')) for i in range(0, 10)]

vetorC = []

for j in range(0, len(vetorA)):
    if j % 2 == 0:
        vetorC.insert(j, vetorA[j])
    else:
        vetorC.insert(j, vetorB[j])

for j in range(0, len(vetorC)):
    print(f'O vetor C: {vetorC[j]}')
