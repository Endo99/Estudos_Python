total = 0
counter = 0
for i in range(0, 100):
    if i % 2 == 0:
        counter += 1
        total += i
    if counter == 50:
        print(total)