n, m = map(int, input().split())

k = list(map(int, input().split()))
j = list(map(int, input().split()))

l = set(k) - set(j)
l = sorted(list(l))
if len(l) == 0:
    print(0)
else:
    print(len(l))
    print(*l)