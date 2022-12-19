n, m = map(int, input().split())

myset = set()
for _ in range(n):
    j = input()
    myset.add(j)

cnt = 0
for _ in range(m):
    i = input()
    if i in myset:
        cnt += 1
        myset.add(i)
print(cnt)
