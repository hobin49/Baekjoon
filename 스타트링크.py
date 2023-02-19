from collections import deque
import sys
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())


#방문 표시를 위해서 사용
visited = [False] * (f+1)

cnt = 0
def bfs(start, end, up, down):
    queue = deque()
    #큐에 처음에 (시작시간, 시간 재기 위한 변수)
    queue.append((start, cnt))


    while queue:
        now, time = queue.popleft()
        #만약에 queue에서 빼냈을 때 도착지점이랑 일치하면 종료
        if now == end:
            return time
        #오르고, 내리는 방법이 있으니까 리스트에 담아두고
        way = [now+up, now-down]
        for w in way:
            #지정된 범위 내에서 그리고 방문하지 않은 곳이면
            if 0 < w <= f and visited[w]==False:
                #방문표시
                visited[w] = True
                #queue에 다음 방문할 곳이랑 시간+1 해줘서 넣어준다
                queue.append((w, time+1))
    #결국 도착지점에 도달하지 못하면 return time 할 것이 없으니 실패구문 작동
    return "use the stairs"

ans = bfs(s, g, u, d)
print(ans)