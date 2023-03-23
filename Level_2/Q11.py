values = input().split(',')
res = []
for v in values:
    intp = int(v, 2)
    if intp % 5 == 0:
        res.append(v)

print(','.join(res))

