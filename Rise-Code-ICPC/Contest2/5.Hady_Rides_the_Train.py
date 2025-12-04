id = int(input())

row = id // 4

if row % 2 == 0:
    col = id % 4
else:
    col = 3 - (id % 4)

print(row, col)
