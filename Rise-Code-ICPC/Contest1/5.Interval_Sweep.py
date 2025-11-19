# E. Interval Sweep

a, b = map(int, input().split())

n = a + b

if n == 0:
    print("NO")
elif n % 2 == 0:
    # even length -> odd and even must be equal
    print("YES" if a == b else "NO")
else:
    # odd length -> counts differ by exactly 1
    print("YES" if abs(a - b) == 1 else "NO")
