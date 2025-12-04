n = int(input())
arr = list(map(int, input().split()))

max_f = 0

for x in arr:
    count = 0
    while x % 2 == 0:
        count += 1
        x //= 2
    max_f = max(max_f, count)

print(max_f)
