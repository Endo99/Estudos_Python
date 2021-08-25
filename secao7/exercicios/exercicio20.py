vetor = []
impares = []

for i in range(0, 10):
    number = int(input('Insira um número: \n'))
    if 0 <= number <= 50:
        vetor.append(number)

for i in range(0, len(vetor)):
    if vetor[i] % 2 == 1:
        impares.append(vetor[i])

print(f'Vetor com 10 posições:')
n = 0
for i in range(0, len(vetor)):
    if len(vetor) > i+1:
        print(f' {vetor[i]} {vetor[i+1]}')

print(f'Vetor com ímpares:')
counter = 0
for i in range(0, len(impares)):
    if len(impares) > i+1:
        print(f'{impares[i]} {impares[i+1]}')