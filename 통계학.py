import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

numbers = [int(input()) for _ in range(n)]

num = sorted(numbers)


def average():
    a = int(sum(num))
    if a >= 0:
        return int(sum(num) / n + 0.5)
    elif a < 0:
        return int(sum(num) / n - 0.5)


def mid_number():
    mid = len(num) // 2
    mid_num = num[mid]

    return mid_num


def most_common_num():
    cnt = Counter(num).most_common(2)

    if len(num) > 1:
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]
    else:
        return cnt[0][0]


def num_range():
    max_ = max(numbers)
    min_ = min(numbers)

    return max_ - min_


print(average())
print(mid_number())
print(most_common_num())
print(num_range())
