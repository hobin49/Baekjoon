import sys
import heapq

input = sys.stdin.readline

t = int(input())
assignment = []
# 입력값들을 받고 튜를로 리스트에 넣어준다.
for _ in range(t):
    d, w = map(int, input().split())
    assignment.append((d, w))

# 정렬을 해준다.
assignment.sort()

# 점수를 담을 리스트
heap = []
# 리스트를 돌면서
for day, point in assignment:
    # 힙푸시를 진행한다.
    heapq.heappush(heap, point)
    # [10, 20, 30, 50, 40] > day= 4
    # heappop을 하면 작은 값을 pop [20, 30, 50, 40]
    # [20, 40, 30, 50, 60] > day =4
    # heappop을 하면 작은 값을 pop [30, 40, 60, 50]
    # [5, 30, 60, 50, 40] 더 이상 리스트에 들어올 값 없고 이들의 핪 185
    # 만약 힙의 길이가 남은 마감일보다 크다면 pop을 해준다.
    if len(heap) > day:
        heapq.heappop(heap)

print(sum(heap))
