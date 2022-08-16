# 입력의 마지막 줄에 0이 주어지기에 while 무한루프를 만든다.
while True:
    #입력값을 받는다.
    w, h = map(int, input().split())

    #만약 너비와 높이 모두 0이면 종료해준다.
    if w == 0 and h == 0:
        break

    #2차원 배열을 만든다.
    maps = [list(map(int, input().split())) for _ in range(h)]

    #팔방탐색을 시작
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    #결과를 담을 변수
    cnt = 0

    def dfs(i, j):
        stack = [(i, j)]

        while stack:
            (x, y) = stack.pop()
            maps[x][y] = 0

            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]

                if -1 < nx < h and -1 < ny < w:
                    if maps[nx][ny] == 1:
                        stack.append((nx, ny))
        
        return 1

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                cnt += dfs(i,j)

    print(cnt)


