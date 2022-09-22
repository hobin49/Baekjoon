from collections import deque

# 입력값 받아주고
n = int(input())

# 이차원 배열 만든다
graph = [list(map(int, input())) for _ in range(n)]



#bfs 만들기 
def bfs(graph, x, y):
    #사방탐색 진행할 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #단지를 세워줄 변수
    cnt = 1
    #덱을 만들어주고
    queue = deque()
    queue.append((x, y))
    #한 번 방문한 곳 재방문 하지 않도록 처리한다
    graph[x][y] = 0


    #큐가 있을때까지
    while queue:
        #큐에 있는 값을 꺼내준다.
        x, y = queue.popleft()
        # 사방탐색을 진행한다.
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            #만약 사방탐색 부분이 범위를 벗어나면 넘어가고
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            #먄약 사방탐색 한 부분이 0이면 넘어간다.
            if graph[nx][ny] == 0:
                continue

            #만약 1을 만나면 count해주고 queue에 추가
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


#모든 리스트 다 돌때까지 돌아준다.
answer = []
for i in range(n):
    for j in range(n):
        #만약 방문할 곳이 있으면 돌아준다.
        if graph[i][j] == 1:
            answer.append(bfs(graph, i, j))

answer.sort()
#출력한다.
print(len(answer))
print(*answer, sep="\n")