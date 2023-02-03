# import sys

# input = sys.stdin.readline


# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])

#     return parent[x]


# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a < b:
#         parent[b] = a

#     else:
#         parent[a] = b


# v, e = map(int, input().split())

# edges = []
# result = 0

# # 부모테이블 초기화
# parent = [0] * (v + 1)

# # 부모테이블에서 부모노드가 자기자신을 가리키도록
# for i in range(1, v + 1):
#     parent[i] = i


# for _ in range(e):
#     a, b, c = map(int, input().split())

#     edges.append((c, a, b))


# edges.sort()


# for edge in edges:
#     cost, a, b = edge

#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost

# print(result)

# 프림 풀이

import heapq
import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = collections.defaultdict(list)

visited = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def prim():
    queue = []
    queue.append([0, 1])
    total = 0

    while queue:
        cost, node = heapq.heappop(queue)

        if visited[node] == 0:
            visited[node] = 1
            total += cost

            for adj in graph[node]:
                heapq.heappush(queue, adj)

    return total


print(prim())
