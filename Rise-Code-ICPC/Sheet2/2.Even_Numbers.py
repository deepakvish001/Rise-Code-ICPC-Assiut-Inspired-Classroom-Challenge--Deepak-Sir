N = int(input())
found = False   # check if any even number printed

for i in range(1, N + 1):
    if i % 2 == 0:   # even number check
        print(i)
        found = True

if not found:
    print(-1)
