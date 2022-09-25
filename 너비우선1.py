from collections import deque
n, m, r = map(int, input().split())

#인접리스트를 만든다.
graph = [[] * n for _ in range(n + 1)]

#인접리스트에 노드의 정보들을 넣어준다.
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#방문체크할 리스트가 필요하다.
visited = [0] * (n + 1)

#방문 순서를 체크할 변수가 필요하다.
cnt = 1

def bfs(x):
    queue = deque([x])
    global cnt 
    #첫 노드 방문표시
    visited[x] = 1

    #queue가 있을떄까지 돌고
    while queue:
        #현재 노드를 꺼내준다.
        now = queue.popleft()
        #간선 순서를 오름차순한다.
        graph[now].sort()
        #인접 노드를 돌면서
        for adj in graph[now]:
            #만약 인접 노드들이 아직 방문하지 않으면 방문처리를 해준다.
            if visited[adj] == 0:
                cnt += 1
                visited[adj] = cnt
                #queue에 인접노드를 돈다.
                queue.append(adj)

#bfs 함수  실행
bfs(r)

#1번 노드부터 방문 순서를 출력
for i in visited[1:]:
    print(i)