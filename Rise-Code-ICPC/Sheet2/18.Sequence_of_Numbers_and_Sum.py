while True:
    try:
        N, M = map(int, input().split())
    except:
        break

    if N <= 0 or M <= 0:
        break

    start = min(N, M)
    end = max(N, M)

    total = 0
    result = []

    for x in range(start, end + 1):
        result.append(str(x))
        total += x

    print(" ".join(result) + f" sum ={total}")
