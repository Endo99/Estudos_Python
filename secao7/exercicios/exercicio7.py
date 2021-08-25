vetor_int = []

for i in range(0, 10):
    vetor_int.append(int(input('Por favor, insira um valor: \n')))

posicao = vetor_int.index(max(vetor_int)) + 1

print(f'Maior elemento: {max(vetor_int)} \n'
      f'Posição: {posicao}')