import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

# 충전에 걸리는 시간을
electronic = sorted(list(map(int, input().split())), reverse=True)

# heapq에 넣기
heap = []
# 충전시간 계산할 변수
for elec in electronic:
    # 만약 힙의 길이가 콘센트 개수보다 작다면 여유가 있는 것으로 heappush
    if len(heap) < m:
        heapq.heappush(heap, elec)
    # 만약 heap의 크기가 최대 콘센트의 개수 만큼 넣어졌을 경우
    # [8, 4] => [8, 8] => [8, 9] => [9, 9] => 답은 9
    elif len(heap) == m:
        # 변수에 heappop을 넣어주고
        time_ = heapq.heappop(heap)
        # 이전까지 충전했던 시간 + 해당 기기를 충전하는데 걸리는 시간을 더한 값을 heap에 넣어준다.
        heapq.heappush(heap, elec + time_)
# 가장 오래 걸린 시간을 출력
print(max(heap))
