N,K = map(int, input().split())
coins = []
count = 0
for number in range(N):
    A = int(input())

    if K >= A: # >하면 안된다
        coins.append(A)
coins.sort(reverse=True)

for coin in coins:
    count += K // coin
    K %= coin

print(count)