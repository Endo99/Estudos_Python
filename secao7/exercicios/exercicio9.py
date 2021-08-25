vetor_par = []

for i in range(0, 6):
    number = int(input('Digite um valor: \n'))
    if number % 2 == 0:
        vetor_par.append(number)

print(f'Os valores pares: {vetor_par} \n'
      f'O vetor pares inverso: {vetor_par[::-1]}')