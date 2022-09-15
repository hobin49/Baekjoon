t = int(input())
lst = []
for _ in range(t):
    n = int(input())
    lst.append(n)

lst = sorted(lst, reverse=True)

print(*lst, sep="\n")