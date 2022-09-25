from collections import deque
#입력값을 받고
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# graph를 만들어준다.
graph = [[0] * n for _ in range(n)]

# 탐색할 리스트를 만든다.
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(x, y):
    #큐에 값을 넣어준다.
    queue = deque([(x, y)])
    #큐가 있을때까지 돌아주면서
    while queue:
        #값을 뺴주고
        x, y = queue.popleft()

        #탐색을 시작하자.
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]

            #만약 범위를 벗어나지 않으면
            if (-1 < nx < n) and (-1 < ny < n) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                if nx == r2 and ny == c2:
                    return graph[nx][ny]
    return -1


print(bfs(r1, c1))
