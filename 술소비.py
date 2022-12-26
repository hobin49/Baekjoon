t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(str, input().split())))

    k = sorted(lst, key=lambda x: -int(x[1]))

    print(k[0][0])
