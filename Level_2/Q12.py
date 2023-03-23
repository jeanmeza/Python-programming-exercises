res = []
for i in range(1000, 3001):
    s = str(i)
    b = True
    for c in s:
        if int(c) % 2 != 0:
            b = False
            break
    if b:
        res.append(s)

print(','.join(res))


