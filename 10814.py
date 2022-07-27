N = int(input())
for tc in range(N):
    name = list(map(str, input().split()))

    k = sorted(name)
    print(k)