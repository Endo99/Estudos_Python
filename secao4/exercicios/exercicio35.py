import math

print('Entre com um valor para o cateto adjacente: ')
a = int(input())
print('Entre com um valor para o cateto oposto: ')
b = int(input())

hipotenusa = math.sqrt((a**2+b**2))

print(f'O valor da hipotenusa é: {hipotenusa}')