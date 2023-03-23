import math

C = 50
H = 30
D = input().split(',')
Q=(math.sqrt((2 * C * int(i))/H) for i in D)

print(math.floor(i) for i in Q)