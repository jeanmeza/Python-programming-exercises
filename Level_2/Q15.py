n = input("Enter a number: ")

f = ['aa', 'aaa', 'aaaa']
res = int(n)
for v in f:
    res += int(v.replace('a', n))

print(res)
