N = int(input())

# Upper part
for r in range(1, N + 1):
    spaces = " " * (N - r)
    stars = "*" * (2 * r - 1)
    print(spaces + stars)

# Lower part
for r in range(1, N + 1):
    spaces = " " * (r - 1)
    stars = "*" * (2 * (N - r + 1) - 1)
    print(spaces + stars)
