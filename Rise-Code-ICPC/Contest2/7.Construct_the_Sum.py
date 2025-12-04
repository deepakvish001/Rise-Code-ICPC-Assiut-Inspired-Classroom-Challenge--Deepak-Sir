t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    
    # Maximum possible sum of 1..n
    max_sum = n * (n + 1) // 2
    
    if s > max_sum:
        print(-1)
        continue
    
    result = []
    
    # Greedily pick largest numbers first
    for x in range(n, 0, -1):
        if s >= x:
            result.append(x)
            s -= x
        
        if s == 0:
            break
    
    print(*result)
