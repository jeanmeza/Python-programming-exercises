def fact(i, acc=1):
    if i == 0:
        return acc
    return fact(i - 1, i * acc)


x = int(input("Enter a number: "))
print(fact(x))
