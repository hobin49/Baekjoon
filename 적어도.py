num = list(map(int, input().split()))
cnt = 0
i = 1
while cnt < 3:
    cnt = 0
    for n in num:
        # 만약 나누어 떨어지면 배수니까 count
        if i % n == 0:
            cnt += 1
        # 개수가 3개 되면 브레이크
        if cnt == 3:
            break
    i += 1
print(i - 1)
