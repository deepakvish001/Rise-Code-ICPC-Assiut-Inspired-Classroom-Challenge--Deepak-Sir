# L. The Brothers
# First person ka first aur second name lo
F1, S1 = input().split()

# Second person ka first aur second name lo
F2, S2 = input().split()

# Agar second names same hain → ARE Brothers
if S1 == S2:
    print("ARE Brothers")
else:
    print("NOT")
