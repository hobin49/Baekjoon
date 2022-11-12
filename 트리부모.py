import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 입력값 받기
n = int(input())

# 그래프 만들기
graph = [[] for _ in range(n + 1)]

# 입력값을 받아준다.
for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


parent = [0 for _ in range(n + 1)]


def dfs(s):
    for i in graph[s]:
        if parent[i] == 0:
            parent[i] = s
            dfs(i)


dfs(1)

for i in range(2, n + 1):
    print(parent[i])
