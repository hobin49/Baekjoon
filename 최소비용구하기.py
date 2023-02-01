import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())


graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for w, dis in graph[now]:
            cost = dist + dis
            if cost < distance[w]:
                distance[w] = cost
                heapq.heappush(q, (cost, w))


n, m = map(int, input().split())

dijkstra(n)

print(distance[m])
