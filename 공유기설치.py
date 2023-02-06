import sys
input = sys.stdin.readline
n, c = map(int, input().split())

router = []
for _ in range(n):
    a = int(input())
    router.append(a)


router.sort()


ans = 0
left = 1

right = router[n-1] - router[0]

distance = 0
ans = 0

while (left <= right):
    start = router[0]
    cnt = 1
    mid = (left+right) // 2

    for i in range(len(router)):
        if router[i] >= start + mid:
            start = router[i]
            cnt += 1

    if cnt >= c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1



print(ans)