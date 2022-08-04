for _ in range(int(input())):
    a = input().split()
    result = []
    for i in a:
        result.append(i[::-1])

    print(*result)