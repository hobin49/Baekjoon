from collections import deque

n, k = map(int, input().split())

# 움직일 수 있는 최대 좌표는 100000
max_coordinate = 100000
#해당 위치에 도착했을 때 시간을 표시하는 리스트
#시작하지 않아서 0으로 시작
visited = [0] * (max_coordinate + 1)

#bfs 함수 정의
def bfs(n):
    #deque에 담아주고 넣어준다.
    queue = deque([n])

    #queue가 있을때까지 돌아주기
    while queue:
        #그 빼준값이 동생의 위치와 일치하면 종료
        now = queue.popleft()
        if now == k:
            break
                
        for move in [now-1, now+1, now*2]:
            