n = list(map(str, input()))

zero, one = 0, 0

for i in range(len(n)):
    if n[i] != n[i - 1]:
        if n[i] == "1":
            one += 1
        else:
            zero += 1

# one or zero 상관 없어
print(zero)
