import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]


def binary_search(n, seconds):
    left = 0
    right = max(seconds) * m

    while left <= right:
        cnt = 0
        mid = (left + right) // 2

        for i in range(n):
            cnt += mid // lst[i]

        if cnt < m:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    return answer

print(binary_search(n, lst))

