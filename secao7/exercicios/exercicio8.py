from typing import List

lista = []

for i in range(0, 6):
    lista.append(int(input('Insira um valor: \n')))

lista_reverse = lista[::-1]
print(f'Ordem normal: {lista} \n'
      f'Oderm inversa: {lista_reverse}')