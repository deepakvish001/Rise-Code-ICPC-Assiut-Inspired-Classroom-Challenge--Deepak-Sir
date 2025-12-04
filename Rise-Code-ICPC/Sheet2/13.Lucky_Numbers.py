A, B = map(int, input().split())

lucky_found = False

for num in range(A, B + 1):
    s = str(num)
    is_lucky = True
    
    for ch in s:
        if ch not in ('4', '7'):
            is_lucky = False
            break
    
    if is_lucky:
        print(num, end=" ")
        lucky_found = True

if not lucky_found:
    print(-1)
