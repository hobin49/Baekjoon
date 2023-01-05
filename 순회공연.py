import heapq

n = int(input())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, input().split())))


lecture = sorted(lecture, key=lambda x: x[1])

# 날짜 세기 위한 변수
heap = []

for p, d in lecture:
    heapq.heappush(heap, p)
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))
