import sys
import heapq

heap = []
input = sys.stdin.readline
n = int(input())

for i in range(n):
    x = int(input())

    if x == 0:

        # 배열이 비어있음 0을 출력
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    # x가 0이 아니라면 배열에 x를 힙 푸시한다.
    else:
        heapq.heappush(heap, x)
