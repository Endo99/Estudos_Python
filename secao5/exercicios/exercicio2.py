import math
numero = int(input('Digite um número: \n'))

if numero > 0:
    square = math.sqrt(numero)
    print(f'A raíz quadrada de {numero} é: {square}')
else:
    print(f'O número {numero} é inválido!')