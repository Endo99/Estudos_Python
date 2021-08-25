numeros_entrada = []

for i in range(1, 6+1):
    numeros_entrada.append(int(input(f'Digite um número {i}: \n')))

soma = 0
impares = 0

pares_digitados = []
impares_digitados = []

for i in range(len(numeros_entrada)):
    if i % 2 == 0:
        pares_digitados.append(numeros_entrada[i])
        soma += numeros_entrada[i]
    else:
        impares_digitados.append(numeros_entrada[i])
        impares += 1

print(f'Números pares digitados: {pares_digitados}')
print(f'Soma dos pares digitados: {soma}')
print(f'Números ímpares digitados: {impares_digitados}')
print(f'Quantidade de ímpares digitados: {impares_digitados}')