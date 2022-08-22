T = int(input())
for _ in range(T):
    birth = list(map(str, input().split()))
    date = birth[1:]
    k_date = date[-1:]
    print(k_date)
    