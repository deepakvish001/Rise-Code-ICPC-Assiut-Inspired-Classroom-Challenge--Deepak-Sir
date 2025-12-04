N = input()

# Reverse string and remove leading zeros
rev = N[::-1].lstrip('0')

if rev == "":
    rev = "0"

print(rev)

# Check palindrome
if N == rev:
    print("YES")
else:
    print("NO")
