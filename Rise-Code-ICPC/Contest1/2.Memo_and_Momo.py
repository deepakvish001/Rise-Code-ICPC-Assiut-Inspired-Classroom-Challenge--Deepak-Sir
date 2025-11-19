# B. Memo and Momo
a, b, k = map(int, input().split())
a_div = (a % k == 0)
b_div = (b % k == 0)
if a_div and b_div:
    print("Both")
elif a_div:
    print("Memo")
elif b_div:
    print("Momo")
else:
    print("No One")
