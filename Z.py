def recursive(n, r, c):
    result = 0

    while n != 0:
        n -= 1
        # 1사분면(예: 1, 0, 0)
        if r < (2**n) and c < (2**n):
            result += (2**n) * (2**n) * 0

        # 2사분면(예: 1, 0, 1)
        elif r < (2**n) and c >= (2**n):
            c -= 2**n
            result += (2**n) * (2**n) * 1

        # 3사분면(예: 1, 1, 0)
        elif r >= (2**n) and c < (2**n):
            r -= 2**n
            result += (2**n) * (2**n) * 2

        # 4분면(예: 1, 1, 1)
        else:
            r -= 2**n
            c -= 2**n
            result += (2**n) * (2**n) * 3
    return result


n, r, c = map(int, input().split())
print(recursive(n, r, c))
