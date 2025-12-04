N = int(input())

for row in range(1, N + 1):
    spaces = " " * (N - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)
