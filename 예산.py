import sys

input = sys.stdin.readline
n = int(input())
k = list(map(int, input().split()))
budget = int(input())
start = 0
# 이부분이 문제
end = max(k)
result = 0
while start <= end:
    # 260
    total = 0
    mid = (start + end) // 2
    for x in k:
        total += min(x, mid)

    if total > budget:
        end = mid - 1
    else:
        start = mid + 1
        result = mid


print(result)

# if sum(k) < budget:
#     print(max(k))
# else:
#     # 260
#     mid = sum(k) // 2
#     for i in range(n):
#         total

#     if total >= budget:
