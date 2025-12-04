import sys
data = sys.stdin.read().strip().split()
t = int(data[0])
ans = []
idx = 1
for _ in range(t):
    L = int(data[idx]); R = int(data[idx+1]); idx += 2
    a = min(L, R)
    b = max(L, R)
    sum_b = b * (b + 1) // 2
    sum_a_minus_1 = (a - 1) * a // 2
    ans.append(str(sum_b - sum_a_minus_1))
print("\n".join(ans))
