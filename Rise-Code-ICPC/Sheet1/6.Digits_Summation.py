# F. Digits Summation
N, M = map(int, input().split())
# Last digits nikalo (modulo 10 se)
last_N = N % 10
last_M = M % 10
# Sum of last digits
result = last_N + last_M
print(result)
