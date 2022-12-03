n, a, b = map(int, input().split())

cnt = 1
while a != b:
    # tc 16 8, 9
    # (자신의 번호 + 1 ) // 2
    a = (a + 1) // 2
    b = (b + 1) // 2
    # 8 -> 4 -> 2 -> 1 -> 1
    # 9 -> 5 -> 3 -> 2 -> 1
    if a == b:
        break

    cnt += 1

print(cnt)
