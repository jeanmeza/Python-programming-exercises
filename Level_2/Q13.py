sentence = input()

letters = 0
numbers = 0
for c in sentence:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        numbers += 1

print(f"LETTERS {letters} DIGITS {numbers}")