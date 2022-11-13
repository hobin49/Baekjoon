import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


parents = [0 for _ in range(n + 1)]


def dfs(s):
    for i in graph[s]:
        if parents[i] == 0:
            parents[i] = s
            dfs(i)


dfs(1)

for i in range(2, n + 1):
    print(parents[i])
