vetor = []
# pensar em como fazer para saber se tem o elemento repetido.
for i in range(0, 20):
    vetor.append(int(input('Insira um valor: \n')))

print(f'Vetor que contém números repetidos: {vetor}')

print(f'Vetor sem repetidos: {set(vetor)}')