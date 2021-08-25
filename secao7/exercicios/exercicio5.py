vetor = [2,5,23,76,78,90,134,51,63,67]

pares = 0

for i in range(0,len(vetor)):
    if i % 2 == 0:
        pares += 1
print(f'O vetor ({vetor}) possui {pares} pares no conjunto')