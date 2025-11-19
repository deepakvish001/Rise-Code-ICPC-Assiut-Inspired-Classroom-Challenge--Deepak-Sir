# H. Two numbers
import math  # math.floor() aur math.ceil() use karne ke liye
A, B = map(int, input().split())
# Division result
div = A / B
# Floor, Ceil, Round nikal lo
floor_val = math.floor(div)
ceil_val = math.ceil(div)
round_val = math.floor(div + 0.5)
# Required output format me print karo
print(f"floor {A} / {B} = {floor_val}")
print(f"ceil {A} / {B} = {ceil_val}")
print(f"round {A} / {B} = {round_val}")
