t = int(input())
k = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in k:
    if v == i:
        cnt += 1

print(cnt)
