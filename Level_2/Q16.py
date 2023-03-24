import math

values = []
for v in input().split(','):
    values.append(int(v))

lst = [x*x for x in values if x % 2 != 0]
print(lst)
