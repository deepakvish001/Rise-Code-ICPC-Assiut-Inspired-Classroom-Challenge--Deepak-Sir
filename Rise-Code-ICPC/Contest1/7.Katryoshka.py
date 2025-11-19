n, m, k = map(int, input().split())

# Step 1: make dolls using mouth (combo 2 or 3)
# Each doll with mouth needs: 1 eye + 1 mouth + 1 body
use_mouth = min(m, k, n)   # we must have at least 1 eye, 1 mouth, 1 body

n -= use_mouth
m -= use_mouth
k -= use_mouth

# Step 2: make dolls without mouth (combo 1)
# Needs: 2 eyes + 1 body
use_no_mouth = min(n // 2, k)

print(use_mouth + use_no_mouth)
