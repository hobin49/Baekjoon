import sys
from collections import deque

input = sys.stdin.readline
# 입력값 받기
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
# 입력값을 받아주고(연결된 두 점과 거리가 3개 존재하므로 n-1을 해야한다.)
for _ in range(n - 1):
    n1, n2, distance = map(int, input().split())
    # (노드 번호, 간선의 길이) 형태를 graph에 담았다.
    # [[], [(2, 2), (4, 3)], [(1, 2)], [(4, 2)], [(3, 2), (1, 3)]]
    graph[n1].append((n2, distance))
    graph[n2].append((n1, distance))

# bfs 함수 만들기
def bfs(start, destination):
    # 시작노드 거리(시작값) 넣어주고
    queue = deque()
    queue.append((start, 0))
    # 방문기록
    visited = [False] * (n + 1)
    # 시작노드 방문처리한다.
    visited[start] = True
    # 큐에 값이 있을때까지 돌아주고
    while queue:
        # 큐에서 요소를 꺼낸다.
        node, distance = queue.popleft()
        # 만약 v가 찾고자하는 노드일 경우 거리를 리턴해준다.
        if node == destination:
            return distance
        # 인접 노드를 돌아준다.
        for adj, j in graph[node]:
            # 만약 방문하지 않은 곳이 아니면
            if not visited[adj]:
                # 방문처리하고
                visited[adj] = True
                # 큐에 (인접노드, 거리 기록)을 넣어준다.
                queue.append((adj, distance + j))


# 거리를 알고 싶으 m개의 노드쌍을 입력 받고 함수를 돌려주고 출력해준다.
for _ in range(m):
    n1, n2 = map(int, input().split())
    print(bfs(n1, n2))
