import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for way, node in graph[now]:
            cost = dist + way
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    return distance


result = [[]]
for i in range(1, n + 1):
    # 거리 배열을 매 반복문 실행 시마다 초기화를 시켜줘야 된다. 그렇게 하지 않으면 최초 실행으로 인해 바뀐 distance를 기준으로 다시 한 번 함수를 실행하게 되기 때문이다.
    distance = [INF] * (n + 1)
    result.append(dijkstra(i))

answer = []
for i in range(1, n + 1):
    answer.append(result[i][x] + result[x][i])


print(max(answer))
