N, K = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
while i < N:
    group = arr[i:i+K]
    print(min(group), end=" ")
    i += K
