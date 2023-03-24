sentence = input()

data = {"upper": 0, "lower": 0}

for c in sentence:
    if c.isupper():
        data["upper"] += 1
    elif c.islower():
        data["lower"] += 1

print(f"UPPER CASE {data['upper']} LOWER CASE {data['lower']}")
