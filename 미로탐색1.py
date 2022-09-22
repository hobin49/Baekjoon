from collections import deque
n, m = map(int, input().split())

graph = []
# 이차원 리스트 만들기
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    #사방탐색 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    #queue에 처음 값 넣어주고
    queue = deque()
    queue.append((x, y))
    #큐가 있을때까지
    while queue:
        #앞에 있는 거 먼저 빼고
        x, y = queue.popleft()
        #사방탐색
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            #만약에 사방탐색한 범위가 범위를 벗어나면
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 만약에 탐색한 범위가 이동할 수 없는 범위면 무시하고
            if graph[nx][ny] == 0:
                continue
            
            #만약에 처음 방문한 경우에만 최단 거리를 기록해준다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    #가장 오른쪽 아래까지의 최단 거리를 반환한다.
    return graph[n - 1][m - 1], 1
    

#BFS를 수행한 겨로가 출력
print(bfs(0, 0))
