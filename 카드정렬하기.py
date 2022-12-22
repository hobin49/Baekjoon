import sys
import heapq

input = sys.stdin.readline

n = int(input())

cards = []
for _ in range(n):
    card = int(input())
    cards.append(card)

# 정렬
heap = sorted(cards)


# 누적값
answer = 0

for _ in range(n - 1):
    # 처음에 가장 작은 값 2개를 빼준다.
    card1, card2 = heapq.heappop(heap), heapq.heappop(heap)
    # 값을 더해주고
    cnt = card1 + card2
    # 누적값
    answer += cnt
    # 더해준 값을 다시 푸쉬해준다.
    heapq.heappush(heap, cnt)

# 누적값 출력
print(answer)
