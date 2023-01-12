t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    # 2
    num = n // h + 1
    # 4
    floor = n % h
    if n % h == 0:
        num = n // h
        floor = h
    print(f"{floor * 100 + num}")


# print(hotel)
# x = j + 1
# hotel[i][j] = (100 * y) + x
