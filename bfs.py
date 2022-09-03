from collections import deque
#입력값을 받아주고
n, m, v = map(int, input().split())
#정점의 개수 만큼 그래프를 만들어주고 1번부터 존재하니까 +1해준다. 
graph = [[] for _ in range(n + 1)]

#bfs와 dfs을 담을 리스트
bfs_lst = []
dfs_lst = []

#방문 체크할 노드를 만들어준다.
visited = [False] * (n + 1) 

#그래프에 값을 담아주고
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


#순서가 뒤죽박주이어서 정렬을 해줘야 한다.
for i in range(1, n + 1):
    graph[i].sort()

#dfs 만들기
def dfs(n):
    #처음 시작하는 노드를 방문표시 해준다.
    visited[n] = True
    #리스트에 넣어준다.
    dfs_lst.append(n)
    #인접한 노드를 돌면서
    for adj in graph[n]:
        #방문하지 않은 노드면 또 돌아준다.
        if not visited[adj]:
            dfs(adj)
#bfs 만들기
def bfs(n):
    #큐에 덱으로 감싸준 노드를 담아주고
    queue = deque([n])
    #방문 표시 한다.
    visited[n] = True

    #큐가 있을때까지 돌면서
    while queue:
        #앞의 요소를 빼주고
        now = queue.popleft()
        #리스트에 넣어준다
        bfs_lst.append(now)
        #인접한 노드를 돌면서 돌지 않은 노드가 있으면
        for adj in graph[now]:
            if not visited[adj]:
                #큐에 추가하고
                queue.append(adj)
                #방문표시 한다.
                visited[adj] = True


#dfs를 돌아주고
dfs(v)
#bfs visited가 하나 더 필요하다.
visited = [False] * (n + 1) 
#bfs를 돌아준다.
bfs(v)
#unpacking 해줘서 방문된 점을 순서대로 출력한다.
print(*dfs_lst)
print(*bfs_lst)
