import sys

sys.setrecursionlimit(10**6)

# dfs
def dfs(x, y):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    for d in range(4):
        nx = dx[d] + x
        ny = dy[d] + y

        if (-1 < nx < h) and (-1 < ny < w):
            if lamb[nx][ny] == "#":
                lamb[nx][ny] = "."
                dfs(nx, ny)


t = int(input())


for _ in range(t):
    h, w = map(int, input().split())
    lamb = []
    for _ in range(h):
        lamb.append(list(map(str, input())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if lamb[i][j] == "#":
                dfs(i, j)
                cnt += 1

    print(cnt)


# bfs
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            if (-1 < nx < h) and (-1 < ny < w):
                if lamb[nx][ny] == "#":
                    lamb[nx][ny] = "."
                    queue.append((nx, ny))


t = int(input())

# 입력값을 받아주고
for _ in range(t):
    h, w = map(int, input().split())
    lamb = []
    for _ in range(h):
        lamb.append(list(map(str, input())))

    # 사방탐색
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    cnt = 0
    for i in range(h):
        for j in range(w):
            # 양을 발견하면 함수를 돈다.
            if lamb[i][j] == "#":
                bfs(i, j)
                # 함수를 돌때마다 count
                cnt += 1

    print(cnt)
