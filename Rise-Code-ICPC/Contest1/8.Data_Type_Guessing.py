n, k, a = map(int, input().split())

num = n * k

# If division produces fractional -> double
if num % a != 0:
    print("double")
else:
    value = num // a

    INT_MIN = -2147483648
    INT_MAX = 2147483647
    LL_MIN = -9223372036854775808
    LL_MAX = 9223372036854775807

    if INT_MIN <= value <= INT_MAX:
        print("int")
    elif LL_MIN <= value <= LL_MAX:
        print("long long")
    else:
        print("double")
