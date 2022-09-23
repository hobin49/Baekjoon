from collections import deque 
n = int(input())

#사방 탐색을 진행해야한다.
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

#방문 표시를 해야한다.
visited = [[False] * n for _ in range(n)]

#그래프르 만들어야 한다.
graph = [[] for _ in range(n)]

#입력값을 받아준다.
for i in range(n):
    color = input()
    for x in color:
        graph[i].append(x)

#dfs 만든다.
def bfs(x, y, color):
    #큐에 값을 넣어주고
    queue = deque([x, y])
    #큐가 있을때까지 돌아준다.
    while queue:
        #x,y로 해서 각각 리스트의 [0, 1]인덱스를 나누어 변수에 할당한다.
        now = queue.popleft()
        x = now[0]
        y = now[1]
        #방문하지 않았으면 방문표시를 해준다.
        if visited[x][y] == False:
            visited[x][y] = True
            #사방탐색 진행
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                #탐색한 범위가 범위를 벗어나지 않고
                if (nx >= 0 and nx < n) or (ny >= 0 and ny > n):
                    # 같은 색깔이면 이동한다.
                    if graph[nx][ny] == color:  
                        queue.append([nx, ny])

#색약이 아닐 때
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = graph[i][j]
            bfs(i, j, graph)
            cnt += 1

#색약일 때
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

cnt_color_weakness = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = graph[i][j]
            bfs(i, j, color)
            cnt_color_weakness += 1

print(cnt)
print(cnt_color_weakness)