N = int(input())


milk = list(map(int, input().split()))

count = 0
for m in range(N):
    if milk[m] == count % 3:
        count += 1

print(count)