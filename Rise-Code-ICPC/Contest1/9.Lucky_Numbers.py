N = int(input())

tens = N // 10
ones = N % 10

if ones != 0 and tens % ones == 0:
    print("YES")
elif tens != 0 and ones % tens == 0:
    print("YES")
else:
    print("NO")
