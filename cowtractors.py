import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, (-c, a, b))


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(node1, node2):
    root1, root2 = find_parent(node1), find_parent(node2)
    if root1 == root2:
        return False
    else:
        parent[root2] = root1
        return True


def kruskal():
    total = 0
    edge_cnt = 0

    while edges:
        cost, node1, node2 = heapq.heappop(edges)
        if union_parent(node1, node2):
            total -= cost
            edge_cnt += 1
            if edge_cnt == n - 1:
                break

    if edge_cnt == n - 1:
        return total
    else:
        return -1


ans = kruskal()
print(ans)
