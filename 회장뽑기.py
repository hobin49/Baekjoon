import sys

input = sys.stdin.readline

INF = sys.maxsize

n = int(input())

friends = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    friends[i][i] = 0


while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    friends[a][b] = 1
    friends[b][a] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

print(friends)

max_number = []

for i in range(1, n + 1):
    max_number.append(max(friends[i][1:]))
min_ = min(max_number)

print(min_, max_number.count(min_))

result = []

for i in range(n):
    if min_ == max_number[i]:
        result.append(i + 1)

print(*result)
