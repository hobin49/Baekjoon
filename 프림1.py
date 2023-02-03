import sys

sys.setrecursionlimit(10**6)
import heapq
import collections

n, m = map(int, input())
graph = collections.defaultdict(list)
visited = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, a, b))
    graph[b].append((c, b, a))


def prim(start):
    visited[start] = 1
    cur = graph[start]
    queue = heapq.heapify(cur)
    total_weight = 0
    q = []

    while queue:
        weight, a, b = heapq.heappop(queue)

        if visited[b] == 0:
            visited[b] = 1
            q.append((a, b))
            total_weight += weight

            for edge in graph[b]:
                if visited[edge[2]] == 0:
                    heapq.heappush(queue, edge)

    return total_weight
