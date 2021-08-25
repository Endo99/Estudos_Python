import math

vetor = [20, 50, 10, 30, 60, 40, 80, 90, 110, 100]

m = sum(vetor) / len(vetor)

desvio = 0
for i in range(len(vetor)):
    desvio += math.sqrt((vetor[i] - m)**2)

print(desvio)