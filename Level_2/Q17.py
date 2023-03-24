net = 0
while True:
    inp = input()
    if not inp:
        break
    tx = inp.split(' ')
    if tx[0] == 'D':
        net += int(tx[1])
    elif tx[0] == 'W':
        net -= int(tx[1])
    else:
        pass

print(net)
