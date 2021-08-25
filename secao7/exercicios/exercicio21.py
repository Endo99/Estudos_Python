A = []
B = []

for i in range(0, 10):
    A.append(int(input(f'Entre com um número {i}: \n')))

for i in range(0, 10):
    B.append(int(input(f'Entre com um número {i}: \n')))

C = []

for i in range(0, len(A)):
    C.append(A[i]+B[i])

for i in range(0, len(C)):
    print(f'{C[i]}')