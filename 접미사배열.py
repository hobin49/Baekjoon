n = input()

lst = []
for i in range(len(n)):
    lst.append(n[i::])

lst = sorted(lst)
print(*lst, sep="\n")
