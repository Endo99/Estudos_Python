A = []

A.append(1)
A.append(0)
A.append(5)
A.append(-2)
A.append(-5)
A.append(7)

B = A[0] + A[1] + A[5]

print(B)

A[4] = 100

print(A)

for i in range(0, len(A)):
    print(A[i])