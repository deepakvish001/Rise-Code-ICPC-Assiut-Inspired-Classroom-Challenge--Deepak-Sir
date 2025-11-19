# Y. The last 2 digits
#3435, 5463, 6733, 8643
A, B, C, D = map(int, input().split())

# Only keep last 2 digits during multiplication
result = (A % 100) * (B % 100)
result %= 100
result = (result * (C % 100)) % 100
result = (result * (D % 100)) % 100

# Print EXACT 2 digits (with leading zero if needed)
print(f"{result:02d}")
