H, M = map(int, input().split())

if H >= 0 and M >= 45:
    print(H, (M - 45))
elif H >= 1 and M < 45:
    print((H -1), (15 + M))
elif H == 0 and M < 45:
    print((23 - H), (15 + M))