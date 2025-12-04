N = int(input())

a, b = 0, 1

for i in range(1, N + 1):
    if i == 1:
        print(a, end=" ")
    elif i == 2:
        print(b, end=" ")
    else:
        c = a + b
        print(c, end=" ")
        a, b = b, c
