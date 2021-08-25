vetor = []
vetor_aux = []

for i in range(0, 10):
    vetor.append(float(input('Digite um valor: \n')))
    vetor_aux.append(vetor[i]**2)

print(vetor_aux)
