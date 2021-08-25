vector = []

for i in range(0, 10):
    vector.append(int(input('Digite um valor: \n')))

print(f'O maior elemento dentro do conjunto é {max(vector)} e o '
      f'menor valor é {min(vector)}')