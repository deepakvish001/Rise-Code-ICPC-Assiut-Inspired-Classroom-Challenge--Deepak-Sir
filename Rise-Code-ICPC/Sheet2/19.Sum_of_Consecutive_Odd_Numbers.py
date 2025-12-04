T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    start = min(X, Y) + 1
    end = max(X, Y)
    
    total = 0
    
    for num in range(start, end):
        if num % 2 == 1:
            total += num
            
    print(total)
