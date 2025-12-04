N = int(input())

mid = N // 2

for i in range(N):
    row = ""
    for j in range(N):
        if i == mid and j == mid:
            row += "X"
        elif i == j:
            row += "\\"
        elif i + j == N - 1:
            row += "/"
        else:
            row += "*"
    print(row)
