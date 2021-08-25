vetorA = [float(input(f'Insira um número real {i}: \n')) for i in range(0, 5)]

vetorB = [float(input(f'Insira um número real {i}: \n')) for i in range(0, 5)]

i = 0
produto_escalar = 0

while i <= 5:
    produto_escalar += (vetorA[i] * vetorB[i])
    i += 1