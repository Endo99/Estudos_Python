notas = []

for i in range(0, 15):
   notas.append(int((input('Entre com a nota do aluno: \n'))))

soma = 0
for i in range(0, len(notas)):
    soma += notas[i]

media = soma / len(notas)

print(f'A média das notas dos alunos são: {media}')