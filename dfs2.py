import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

cnt = 1


def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    graph[v].sort(reverse=True)

    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)


dfs(graph, r, visited)

for k in visited[1:]:
    print(k)
