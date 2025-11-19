# Z. Hard Compare

import math

A, B, C, D = map(int, input().split())

left = B * math.log(A)
right = D * math.log(C)

if left > right:
    print("YES")
else:
    print("NO")
