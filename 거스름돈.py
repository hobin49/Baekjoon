n = int(input())
cnt = 0
thsouand = 1000
lst = [500, 100, 50, 10, 5, 1]

now = []
k = 0
check = thsouand - n
for coin in lst:
    cnt += check // coin
    check %= coin

print(cnt)
