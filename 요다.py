n = int(input())
result = []
for _ in range(n):
    k = list(map(str, input().split()))

    k1 = k.pop(0)
    k.append(k1)
    k2= k.pop(0)
    k.append(k2)

    print(*k)