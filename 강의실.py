import sys
import heapq

input = sys.stdin.readline

t = int(input())
rooms = []
for _ in range(t):
    start, end = map(int, input().split())
    rooms.append((start, end))
# 강의시간 정렬
rooms = sorted(rooms)
heap = []
# 첫 번째 강의가 끝나는 시간을 우선순위 큐에 추가
heapq.heappush(heap, rooms[0][1])

# 강의 리스트의 1번째 인덱스부터 마지막 인덱스까지 반복문을 실행한다
for i in range(1, len(rooms)):
    # 우선순위 큐에 첫 번째 인덱스에 접근(항상 끝나는 시간이 가장 빠른 순)
    k = heap[0]
    # 만약 강의의 시작시간이 우선순위 큐의 첫 번째 인덱스보다 작다면 해당 강의 끝나는 시간을 우선순위 큐에 추가
    # [2, 4]에서 [2]는 k인 [3]보다 작다 따라서 heap에 종료 시간인 [4]가 들어간다. [3,4]
    if rooms[i][0] < k:
        heapq.heappush(heap, rooms[i][1])
        print(heap)
    # 아니라면 우선순위 큐의 첫 번째 인덱스를 pop한 후 해당 강의의 끝나는 시간을 우선순위 큐에 추가한다.
    # [3, 5]에서 3은 k보다 작지 않으므로 k를 pop해주고 대신 3의 종료시간 5를 넣어준다.
    # 최종적으로 [4, 5]가 된다.
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, rooms[i][1])
# 총 길이는 필요한 강의실 개수만큼이 된다.
print(len(heap))
