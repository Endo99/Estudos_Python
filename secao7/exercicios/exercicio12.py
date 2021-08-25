array = []
media = 0
maior = 0
menor = 0
for i in range(0, 5):
    array.append(int(input('Insira um número: \n')))
    for j in range(0, len(array)):
        maior = max(array)
        menor = min(array)

for i in range(0, len(array)):
    media += array[i] / len(array)

print(f'O maior número: {maior} \n'
      f'O menor número: {menor} \n'
      f'A média: {media}')