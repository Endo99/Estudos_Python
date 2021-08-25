counter = 0
for i in range(0, 100):
    if i % 3 == 0 and i > 0:
        counter += 1
        print(f'{i} é multiplo de 3')
    if counter == 5:
        break;