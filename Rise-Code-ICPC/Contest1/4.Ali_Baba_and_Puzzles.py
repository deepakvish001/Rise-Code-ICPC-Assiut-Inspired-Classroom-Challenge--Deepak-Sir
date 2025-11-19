# D. Ali Baba and Puzzles (fixed: operators must be distinct)

a, b, c, d = map(int, input().split())

ops = ['+', '-', '*']

def apply(x, op, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    return x * y

def eval_expr(a, op1, b, op2, c):
    # Respect normal precedence: '*' before '+' and '-'
    if op1 == '*' and op2 == '*':
        return (a * b) * c
    if op1 == '*':
        temp = a * b
        return apply(temp, op2, c)
    if op2 == '*':
        temp = b * c
        return apply(a, op1, temp)
    # no '*' so left-to-right
    return apply(apply(a, op1, b), op2, c)

ok = False
for op1 in ops:
    for op2 in ops:
        if op1 == op2:
            continue  # each operator can be used only once (must be distinct)
        if eval_expr(a, op1, b, op2, c) == d:
            ok = True
            break
    if ok:
        break

print("YES" if ok else "NO")
