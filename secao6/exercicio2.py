print('For:')

for i in range(1, 100):
    print(f'{i}')

print('While:')
i = 1
while i != 100:
    print(f'{i}')
    i += 1

print('Do... While')

j = 1
while True:
    if j == 100:
        break
    else:
        print(f'{j}')
        j += 1
