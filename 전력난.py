import sys

input = sys.stdin.readline


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


while True:
    n, m = map(int, input().split())
    if m == 0 and n == 0:
        break

    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    edges = []

    for i in range(m):
        x, y, z = map(int, input().split())

        edges.append((z, x, y))

    edges.sort()

    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
        else:
            result += cost

    print(result)
