vetor = []

for i in range(0, 50):
    vetor.append((i+5*i) % (i+1))

for i in range(0, len(vetor)):
    print(vetor[i])