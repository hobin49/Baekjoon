n = int(input())

car = list(map(int, input().split()))
cnt = 0
for c in car:
    if c == n:
        cnt += 1

print(cnt)
