t = int(input())
lst = []
for _ in range(t):
    n = int(input())
    lst.append(n)
lst.sort()

print(*lst, sep="\n")