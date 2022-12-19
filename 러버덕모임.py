import sys
from itertools import permutations

input = sys.stdin.readline
n, p, e = map(int, input().split())

people = [0] * (n - p)

numbers = []
for _ in range(n):
    x, y = map(int, input().split())
    for k in range(x, y):
        numbers.append(k)

result = []
for k in permutations(numbers, p):
    if sum(k) == e:
        result.append(k)
        people.extend(k)
        print(*people)
        break
else:
    print(-1)


# cnt = 0
# while len(result) != n:
#     if len(result) == n:
#         print(result)
#         break
#     result.append(0)
#     cnt += 1

# print(result)
