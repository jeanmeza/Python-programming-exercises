import math

C = 50
H = 30
D = input().split(',')

values = []
for d in D:
    values.append(str(int(round(math.sqrt(2*C*float(d)/H)))))

print(','.join(values))
