# T. Sort Numbers

A, B, C = map(int, input().split())
# Sort ke liye list banao
arr = [A, B, C]
# 1. Ascending order me print karo
for x in sorted(arr):
    print(x)
# 2. Blank line
print()
# 3. Original order me print karo
print(A)
print(B)
print(C)
