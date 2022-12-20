from collections import deque

m, n, k = map(int, input().split())
# 그래프 만들기
# 사방탐색 위한 dx,dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [[0] * n for _ in range(m)]

# 입력값 받기 좌표니까
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    # 내가 몰랐던 좌표처리
    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[k][j] = 1
            print(graph)


result = []


def bfs(x, y):
    # 넓이 계산
    cnt = 1
    # 영역의 개수 담을 리스트
    queue = deque()
    # 초기값 넣어주고
    queue.append([x, y])
    # 방문 처리
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()
        # 사방탐색
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위가 벗어나지 않는지 체크
            if 0 <= nx < m and 0 <= ny < n:
                # 방문 안하는 곳이면 방문처리
                if graph[nx][ny] == 0:
                    # 방문처리
                    graph[nx][ny] = 1
                    # 넓이 누적
                    cnt += 1
                    # 다음 돌기 위해서 queue에 넣어줍니다.
                    queue.append([nx, ny])

    result.append(cnt)


for a in range(m):
    for b in range(n):
        if graph[a][b] == 0:
            bfs(a, b)

print(len(result))
result.sort()

for r in result:
    print(r, end=" ")
