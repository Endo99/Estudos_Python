n = int(input('Entre com um número: \n'))

count = 0
for i in range(0, n):
    if i % 2 == i:
        if count <= 4:
            print({i})
    count += 1