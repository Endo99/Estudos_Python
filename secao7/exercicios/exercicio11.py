vetor = []

for i in range(0, 10):
    vetor.append(float(input('Insira um valor: \n')))

negativo = 0
soma_positivo = 0
for i in range(0, len(vetor)):
    if i < 0:
        negativo += 1
    else:
        soma_positivo += vetor[i]

print(f'Quantidades de valores negativos encontrado no conjunto: {negativo}\n'
      f'Soma dos positivos encontrados no conjunto: {soma_positivo}')
