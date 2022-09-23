from collections import deque

# 입력값 받기
n, m, k, x = map(int, input().split())

#그래프 만들기
graph = [[] for _ in range(n + 1)]

#입력값 넣기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


#거리 측정하기 위한 리스트
distance = [-1] * (n + 1)

#출발 도시까지의 거리는 0으로 설정
distance[x] = 0

#큐가 있을때까지 돌려주고
def bfs(graph, x, distance):
    #큐에 넣어준다
    queue = deque([x])

    while queue:
        #앞의 노드를 뺴준다.
        now = queue.popleft()

        #인접한 노드를 돌아준다.
        for next in graph[now]:
            #만약 다음 거리가 -1이면 
            if distance[next] == -1:
                #값을 갱신해준다.
                distance[next] = distance[now] + 1
                queue.append(next)

bfs(graph, x, distance)

#최단 거리가 k인 도시를 찾고 아예 없다면 -1을 출력해야한다.
flag = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        flag = True

if flag == False:
    print(-1)
