# W. Mathematical Expression
A, S, B, _, C = input().split()
A = int(A)
B = int(B)
C = int(C)
# Actual correct result
if S == '+':
    result = A + B
elif S == '-':
    result = A - B
else:  # S == '*'
    result = A * B
# Check correctness
if result == C:
    print("Yes")
else:
    print(result)
