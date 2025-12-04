import math

X = int(input())

is_prime = True

for i in range(2, int(math.sqrt(X)) + 1):
    if X % i == 0:
        is_prime = False
        break

if is_prime:
    print("YES")
else:
    print("NO")
