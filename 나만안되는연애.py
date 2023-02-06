import sys
input = sys.stdin.readline

n, m = map(int, input().split())

gender_univ = list(map(str, input().split()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i



graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    if gender_univ[a-1] != gender_univ[b-1]:
        graph.append((c, a, b))


graph.sort()





edge_count = 0
result = 0
for g in graph:
    cost, a, b = g
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        edge_count += 1


if edge_count == n-1:
    print(result)
else:
    print(-1)