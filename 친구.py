import sys
input = sys.stdin.readline

n = int(input())

for i in range 

friends = [list(input()) for _ in range(N)]

for i in range(1, n + 1):
    friends[i][i] = 0

for _ in range(n):
    people = input()


print(friends)
# for k in range(1, n+1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][i])


# for i in range(1, n + 1):
