# 접근 방법
# 1.모든 경우의 수를 다 고려해서 그 중에서 최대 아이템 개수를 최대 아이템 개수를 찾는다
# 2.노드를 거쳐서 가는 경우도 고려해야한다.
# 3.가능한 얻을 수 있는 개수를 다 얻어야하니 최단 경로를 구하자.
# 4-1. 다익스트라의 알고리즘 경우 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단경로
# 4-2. 플로이드-워셜 알고리즘의 경우 모든 정점 사이의 최단 경로를 찾는 알고리즘
# 5. 최단 경로를 탐색하는 과정에서 수색범위를 벗어나지 않는 범위 내에서 아이템 개수를 누적시키고 그 중 최대 아이템을 찾는다.

# [[1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
# [1000000000, 0, 3, 6, 5, 7],
# [1000000000, 3, 0, 3, 8, 4],
# [1000000000, 6, 3, 0, 11, 7],
# [1000000000, 5, 8, 11, 0, 12],
# [1000000000, 7, 4, 7, 12, 0]]

# 플로이드 워셜

# n, m, r = map(int, input().split())

# items = list(map(int, input().split()))

# import sys

# INF = sys.maxsize

# # 1번부터 시작
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for _ in range(r):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c


# # 플로이드 워셜 핵심 자기자신이 자기자신으로 이동하는 경우 0으로 처리한다.
# for i in range(1, n + 1):
#     graph[i][i] = 0


# # 플로이드 워셜 핵심(1~5번 노드)
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if graph[i][j] > graph[i][k] + graph[k][j]:
#                 graph[i][j] = graph[i][k] + graph[k][j]

# # 최댓값을 비교하기 위한 임시 변수
# max_ = 0
# # 시작지점 방문지점 확인하면서
# for i in range(1, n + 1):
#     # 각 정점에서 얻을 수 있는 아이템 개수 중 최댓값을 찾기 위해서 노드가 변할때마다 리셋해준다.
#     temp = 0
#     for j in range(1, n + 1):
#         # 수색범위를 벗어나지 않는 값
#         if graph[i][j] <= m:
#             # 리스트에는 시작이 0번째 인덱스이다.
#             temp += items[j - 1]

#     max_ = max(max_, temp)

# print(max_)


# 또 다른 풀이 (다익스트라)
import heapq
import collections

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = collections.defaultdict(list)

for _ in range(r):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])


def dijkstra(start):
    items_sum = 0
    visit = []
    q = []
    # [거리, 노드]
    heapq.heappush(q, [0, start])
    while q:
        # 거리, 노드
        dist, cur = heapq.heappop(q)
        # 노드가 방문하지 않은 곳이면
        if cur not in visit:
            # 탐색 종료
            if dist > m:
                continue
            # 아이템을 누적한다.
            items_sum += items[cur - 1]
            # 방문 처리
            visit.append(cur)
            # 인접한 노드를 돌면서 (nx= 인접한 노드, w = 거리)
            for nx, w in graph[cur]:
                heapq.heappush(q, [dist + w, nx])
    return items_sum


answer = 0
for i in range(n):
    answer = max(answer, dijkstra(i + 1))
print(answer)
