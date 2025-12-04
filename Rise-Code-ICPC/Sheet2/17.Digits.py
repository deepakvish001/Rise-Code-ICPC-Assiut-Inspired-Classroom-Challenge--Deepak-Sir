T = int(input())

for _ in range(T):
    N = input().strip()
    
    # Reverse string
    rev = N[::-1]
    
    # Print with space between digits
    print(" ".join(rev))
