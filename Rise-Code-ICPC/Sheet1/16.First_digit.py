# P. First digit !

# Input lo (string ke form me taaki pehla digit easily mile)
X = input()

# Pehla digit lo aur integer me badlo
first_digit = int(X[0])

# Check karo even hai ya odd
if first_digit % 2 == 0:
    print("EVEN")
else:
    print("ODD")
