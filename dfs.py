import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


check = [0] * (n + 1)

cnt = 1


def dfs(graph, v, check):
    global cnt
    check[v] = cnt

    graph[v].sort()
    for i in graph[v]:
        if check[i] == 0:
            cnt += 1
            dfs(graph, i, check)


dfs(graph, r, check)

for k in check[1:]:
    print(k)
