# Q. Coordinates of a Point

# Input lo (floats kyunki decimal ho sakte hain)
X, Y = map(float, input().split())

# Conditions check karo (same order Codeforces ke hisaab se)
if X == 0 and Y == 0:
    print("Origem")
elif X == 0:
    print("Eixo Y")
elif Y == 0:
    print("Eixo X")
elif X > 0 and Y > 0:
    print("Q1")
elif X < 0 and Y > 0:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X > 0 and Y < 0:
    print("Q4")
