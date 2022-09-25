from collections import deque
from itertools import count
#입력 값을 받아준다.
n, m, r = map(int, input().split())

#인접리스트를 만들어서 넣어준다.
graph = [[] * n for _ in range(n+1)]

#인접리스트에 값을 넣어준다.
#간선의 수만큼 돌면서
for _ in range(m):
    #입력 값을 받아준다.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#방문한 노드를 체크해야한다.
visitied = [0] * (n + 1)
def bfs(x):
    #큐에 출발 노드를 넣어준다.
    queue = deque([x])
    #시작 노드를 방문체크한다.
    visitied[x] = 1
    #큐에 요소가 있을떄까지 다 돌아준다.
    #시작점의 방문순서는 1이다.
    cnt = 1
    while queue:
        #앞의 요소를 뺴준다.
        now = queue.popleft()
        #간선순서를 내림차순해준다.
        graph[now].sort(reverse=True)
        #인접 노드를 돌면서
        for adj in graph[now]:
            #만약 방문하지 않은 노드면
            if visitied[adj] == 0:
                #순서 체크를 위해서 1씩 더한다.
                cnt += 1
                # 방문체크하고 queue에 인접 노드를 넣어준다.
                visitied[adj] = cnt
                queue.append(adj)

#bfs함수를 돌아준다.
bfs(r)

#노드를 출력한다.
for i in visitied[1:]:
    print(i)


        