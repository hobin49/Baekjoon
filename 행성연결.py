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


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n + 1)]
edges = []

for i in range(1, n):
    for j in range(i):
        edges.append((arr[i][j], i, j))

edges.sort()

result = 0
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c

print(result)
