from collections import deque

n = int(input())

queue = deque((n, [n]))

visited = [False] * (n + 1)
while queue:
    q, q1 = queue.popleft()

    if q == 1:
        print(len(q1))
        print(*q1)
        break
    if not visited:
        visited[q] = True
        if q % 2 == 0:
            queue.append((q // 2, q1 + [q // 2]))
        if q % 3 == 0:
            queue.append((q // 3, q1 + [q // 3]))
        queue.append((q - 1, q1 + [q - 1]))
