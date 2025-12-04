import math

N = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for num in range(2, N + 1):
    if is_prime(num):
        print(num, end=" ")
