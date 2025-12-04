#import math

#A, B = map(int, input().split())
#print(math.gcd(A, B))


A, B = map(int, input().split())

while B != 0:
    A, B = B, A % B

print(A)
