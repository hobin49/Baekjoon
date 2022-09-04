K, N , M = map(int, input().split())

money = (K * N)

if money < M:
    print(0)

else:
    print(money - M)