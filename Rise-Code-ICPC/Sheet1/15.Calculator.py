# O. Calculator
# Input lo (jaise "7+54" ya "17*10")
expr = input()
# Operator check karke split karo
if '+' in expr:
    A, B = expr.split('+')
    print(int(A) + int(B))
elif '-' in expr:
    A, B = expr.split('-')
    print(int(A) - int(B))
elif '*' in expr:
    A, B = expr.split('*')
    print(int(A) * int(B))
elif '/' in expr:
    A, B = expr.split('/')
    print(int(A) // int(B))  # integer division
