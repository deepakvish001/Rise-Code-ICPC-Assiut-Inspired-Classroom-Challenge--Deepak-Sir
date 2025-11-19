# V. Comparison

A, S, B = input().split()
A = int(A)
B = int(B)

if S == '<':
    print("Right" if A < B else "Wrong")
elif S == '>':
    print("Right" if A > B else "Wrong")
else:  # S == '='
    print("Right" if A == B else "Wrong")
