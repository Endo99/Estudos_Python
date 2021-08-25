vetor = []

for i in range(0, 5):
    vetor.append(int(input('Insira um número: \n')))

maior = vetor.index(max(vetor)) + 1
menor = vetor.index(min(vetor)) + 1

print(f'O maior número se encontra no índice: {maior}\n'
      f'O menor número se encontra no índice: {menor}')