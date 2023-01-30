import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] * (n + 1) for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for w, dis in graph[now]:
            cost = dist + dis
            if cost < distance[w]:
                distance[w] = cost
                heapq.heappush(q, (cost, w))


dijkstra(start)


for i in range(1, n + 1):
    print("INF" if distance[i] == INF else distance[i])
