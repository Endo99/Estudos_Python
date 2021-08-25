lista = {}

for i in range(0, 3):
    numero = int(input(f'Insira um número {i+1}: \n'))
    altura = float(input(f'Insira a altura do Aluno {i+1}: \n'))
    if numero in lista.keys():
        print('O número já existe!')
        continue
    else:
        lista[numero] = altura
print(lista)

for numero, altura in lista.items():
    if lista[numero] == min(lista.values()):
        print(f'Número do aluno mais alto: {numero}, Altura: {altura}')
    elif lista[numero] == max(lista.values()):
        print(f'Número do aluno mais baixo: {numero}, Altura: {altura}')