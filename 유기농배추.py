# 재귀 limit 설정 런타임 에러 발생해서...
import sys
sys.setrecursionlimit(10000)

#dfs 만들기
def dfs(x, y):
    #팔방탐색 시작
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    #탐색 시작
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        #만약 탐색한 범위가 배추밭을 벗어나지 않는지 확인
        if (-1 < nx < M) and (-1 < ny < N):
            #만약 배추가 인접할때 체크해준다.
            if graph[ny][nx] == 1:
                #1을 발견하면 -1을 해줘서 0을 만든다
                graph[ny][nx] = -1
                dfs(nx, ny)

#테스트 케이스
T = int(input())

#테스트 케이스만큼 돌면서
for i in range(T):
    #가로, 세로, 개수 입력 받기(정점의 개수, 간선의 개수)
    M, N, K = map(int, input().split())
    #결과 값을 담을 변수
    cnt = 0

    #가로와 세로를 이용해서 그래프를 만든다.
    graph = [[0]* M for i in range(N)]

    #배추 위치에 1을 표시한다.
    #예제 2번의 경우
    #[[0, 0, 0, 0, 1], [0, 0, 0, 0, 0 ], [1, 1, 1, 1, 1]]
    for j in range(K): 
        X, Y = map(int, input().split())
        # 행과 열을 바꿔줘야한다 안그러면 index out of range 발생
        graph[Y][X] = 1
    
    #그래프를 돌면서 배추들이 몇 군데 퍼져있는지 조사
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                #배추가 심어져 있는 땅을 확인해서 
                dfs(x, y)
                #필요한 배추 흰지렁이를 구해준다
                cnt += 1


    print(cnt)
        

