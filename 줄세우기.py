# import sys

# input = sys.stdin.readline

# n = int(input())

# children = list(map(int, input().split()))

# idx = [i for i in range(len(children)+1)]


# z = list(zip(children, idx))

# new = sorted(z, key=lambda x:x[0])

# result = []
# cnt = 0

# for i in range(len(new)-1):
#     if (new[i+1][0] - new[i][0]) == 1 and (new[i+1][1] > new[i][1]):
#         cnt += 1
#         result.append(cnt)
#     else:
#         cnt = 1
#         result.append(cnt)


# if n != 1:
#     print(n - max(result))
# else:
#     print(0)

import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

def line():
    idx = [-1] * (n + 1)

    for i, x in enumerate(nums):
        idx[x] = i

    longest = 0
    cnt = 0
    for num in range(1, n):
        if idx[num] < idx[num+1]:
            cnt += 1

        else:
            longest = max(longest, cnt)
            cnt = 1

    if n!= 1:
        return n - longest
    else:
        return 0

print(line())