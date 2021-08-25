array = []

for i in range(10):
    array.append(int(input(f'Insira um número {i+1}: \n')))

for i in array:

    divisor = 0

    for j in range(1, i+1):
        if i % j == 0:
            divisor += 1

    if divisor <= 2:
        print(f'Elemento = {i} -> Posição = {array.index(i)}')