import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
max_ = 100001
INF = sys.maxsize

def move(x):
    yield(x + 1, 1)
    yield(x - 1, 1)
    yield(x * 2, 0)

def dijkstra(start, k):
    visited = [INF] * (max_)
    q = []
    visited[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        time, node = heapq.heappop(q)

        if time > visited[node]:
            continue

        for cur_move, cur_time in move(node):
            new_time = time + cur_time

            if 0 <= cur_move < max_ and new_time < visited[cur_move]:
                visited[cur_move] = new_time
                heapq.heappush(q, (new_time, cur_move))

    return visited[k]


print(dijkstra(n, k))





