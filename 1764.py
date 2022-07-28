n,m = map(int, input().split())
name1 = set()
for tc in range(n):
    name1.add(input())

name2 = set()
for tc1 in range(m):
    name2.add(input())

name_ = name1 & name2


print(len(name_), *sorted(name_), sep = "\n")