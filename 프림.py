from queue import PriorityQueue

# adj는 가중치를 포함하는 인접리스트의 형태의 그래프이고 start는 prim 알고리즘의 시작정점
def prim(adj, start):
    # 최소 신장 트리에 이미 포함된 정점을 표시하기 위해 covered변수를 set으로 선언한다.
    covered = set()

    # prim 알고리즘의 결과 그래프를 간선들의 목록으로 return하기 위해 res_edges 변수를 list로 선언한다.
    res_edges = []

    # 후보 간선들을 관리할 우선순위큐를 queue변수에 선언한다.
    queue = PriorityQueue()

    # 후보 간선들은 (간선의 가중치, 도착 정점, 시작 정점)으로 표현된다.
    # start 정점에서 알고리즘을 시작하도록 아래처럼 넣는다.
    queue.put((0, start, None))

    while not queue.empty():
        u_cost, u, u_src = queue.get()
        # 맘닐 정점 u가 최소신장트리에 이미 포함되어 있으면 이 간선은 MST에 cycle을 만들기 때문에 무시한다.
        if u in covered:
            continue
        # 이 시점에 정점 u를 최소신장트리에 포함시키는 것이기 때문에 covered에 u를 넣어서 MST에 정점 u가
        # 포함되었다고 표시

        covered.add(u)

        # 정점 u와 연결하는 현재의 간선을 res_edges에 추가
        # u_src 변수가 none일 경우 간선이 아닌 최초 queue에 넣어둔 특수한 값이기 때문에 무시한다.
        if u_src is not None:
            res_edges.append((u_cost, u, u_src))

        # 정점 u와 연결된 모든 간선 (u, v)중에 v가 최소신장트리에 포함되지 않은경우에만 cost와 함께 queue에 넣어준다.
        for v_cost, v in adj[u]:
            # v가 최소신장에 포함되는 간선은 cycle을 만들기에 넣지 않는다.
            if v not in covered:
                queue.put((v_cost, v, u))

    return res_edges


# [(29, '2', '1'), (34, '6', '2'), (23, '4', '6'), (7, '3', '4'), (13, '7', '4'), (53, '5', '6')]

adj = {
    "1": [(29, "2"), (75, "5")],
    "2": [(29, "1"), (35, "3"), (34, "6")],
    "3": [(35, "2"), (7, "4")],
    "4": [(7, "3"), (23, "6"), (13, "7")],
    "5": [(75, "1"), (53, "6")],
    "6": [(34, "2"), (23, "4"), (53, "5"), (25, "7")],
    "7": [(13, "4"), (25, "6")],
}


edges = prim(adj, "1")

cost_sum = 0
for u_cost, u, v in edges:
    print((u_cost, u, v))
    cost_sum += u_cost

print(cost_sum)

# import heapq
# import collections
# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = collections.defaultdict(list)  # 빈 그래프 생성
# # 노드의 방문 정보 초기화
# visited = [0] * (n + 1)

# # 무방향 그래프 생성
# for i in range(m):
#     u, v, weight = map(int, input().split())
#     graph[v].append([weight, u, v])
#     graph[v].append([weight, v, u])


# def prim(graph, start_node):
#     # 방문 갱신
#     visited[start_node] = 1
#     # 인접 간선 추출
#     candidate = graph[start_node]
#     # 우선순위 큐 생성
#     heapq.heapify(candidate)
#     # 최소스패닝트리 리스트
#     mst = []
#     # 전체 가중치
#     total_weight = 0

#     while candidate:
#         weight, u, v = heapq.heappop(candidate)
#         # 방문하지 않았다면
#         if visited[v] == 0:
#             # 방문 갱신
#             visited[v] = 1
#             # mst 삽입
#             mst.append((u, v))
#             # 전체 가중치 갱신
#             # 다음 인접 간선 탐색
#             total_weight += weight
#             for edge in graph[v]:
#                 # 방문한 노드가 아니라면(순환 방지)
#                 if visited[edge[2]] == 0:
#                     # 우선순위 큐에 edge 삽입
#                     heapq.heappush(candidate, edge)

#     return total_weight


# edges = prim(graph, 1)

# print(edges)

# cost_sum = 0
# print(edges)
# for u_cost, u, v in edges:
#     print((u_cost, u, v))
#     cost_sum += u_cost

# print(cost_sum)


# import collections
# import heapq

# graph = collections.defaultdict(list)  # 빈 그래프 생성
# # n, m = map(int, input().split())  # 노드 수, 간선 수
# visited = [0] * (8)  # 노드의 방문 정보 초기화


# # for i in range(m):  # 간성 정보 입력 받기
# #     u, v, weight = map(int, input().split())
# #     graph[u].append([weight, u, v])
# #     graph[v].append([weight, v, u])


# def prim(tree, start):
#     queue = []
#     heapq.heappush(queue, (0, start))  # 비용, 노드
#     sum_ = 0

#     while queue:
#         weight, u, v = heapq.heappop(queue)
#         if visited[v]:  # 큐에 같은 노드가 여러번 들어가있을 수 있으므로 한번 더 체크 필수
#             continue
#         else:
#             visited[v] = True
#             sum_ += weight

#         for nextV in tree[v]:  # 다음노드, 비용
#             if not visited[nextV[0]]:
#                 heapq.heappush(queue, (nextV[1], nextV[0]))
#     return sum_


# tree = {
#     "1": [(29, "2"), (75, "5")],
#     "2": [(29, "1"), (35, "3"), (34, "6")],
#     "3": [(35, "2"), (7, "4")],
#     "4": [(7, "3"), (23, "6"), (13, "7")],
#     "5": [(75, "1"), (53, "6")],
#     "6": [(34, "2"), (23, "4"), (53, "5"), (25, "7")],
#     "7": [(13, "4"), (25, "6")],
# }

# print(prim(graph, "1"))
