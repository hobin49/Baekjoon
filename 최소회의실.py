import sys
import heapq


input = sys.stdin.readline

t = int(input())
rooms = []

for _ in range(t):
    start, end = map(int, input().split())
    rooms.append((start, end))

rooms = sorted(rooms)
heap = []

# 40
heapq.heappush(heap, rooms[0][1])

for i in range(1, len(rooms)):
    # 40
    k = heap[0]

    if rooms[i][0] < k:
        heapq.heappush(heap, rooms[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, rooms[i][1])

print(len(heap))
