# J. Multiples

A, B = map(int, input().split())

# Check karo multiples hain ya nahi
if A % B == 0 or B % A == 0:
    print("Multiples")
else:
    print("No Multiples")
