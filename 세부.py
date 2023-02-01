import sys
import heapq

input = sys.stdin.readline


n, m = map(int, input().split())

start, end = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))


def dijkstra():
    q = []
    heapq.heappush(q, (-sys.maxsize, start))

    while q:
        cost, now = heapq.heappop(q)
        cost = -cost

        if distance[now] > cost:
            continue

        for nway, nnode in graph[now]:
            temp = min(cost, nway)
            if distance[nnode] < temp:
                distance[nnode] = temp
                heapq.heappush(q, (-temp, nnode))


dijkstra()
print(distance[end])
