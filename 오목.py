#먼저 델타 탐색에 필요한 방향 설정이 담긴 dx, dy를 만들어준다. 우, 하, 우하, 우상
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

#이차원 배열을 만들 입력값을 받아준다. 
n = 19

#이차원 배열을 받아준다.
board = [list(map(int, input().split())) for _ in range(n)]
#무승부가 발생했을 때 필요한 변수
answer = 0

#이중 반복문으로 배열을 돌아준다.
for x in range(n):
    for y in range(n):
        #만약 탐색하는 범위에 흰돌이나 검은돌이 있으면 탐색을 해준다.
        if board[x][y] == 1 or board[x][y] == 2:
            #델타탐색을 실행해준다.
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                #델타탐색 할때마다 돌의 개수를 세야하는 변수가 필요하다.
                stone_count = 1 
                
                #while문을 돌면서 
                while True:
                    # 2가지 조건이 필요하다. 1.델타 탐색의 범위가 오목판을 벗어나지 말아야하며
                    if not(-1 < nx < n and -1 < ny < n):
                        break

                    #2.델타탐색해서 얻은 돌과 기존 오목판의 돌의 색깔이 같아야한다.
                    if not(board[x][y] == board[nx][ny]):
                        break
                    
                    # 위 두 조건이 일치하지 않으면 같은 방향 다른 좌표를 탐색한다.
                    nx = nx + dx[d]
                    ny = ny + dy[d]

                    #돌의 개수를 count 해준다.
                    stone_count += 1

                #만약 돌이 5개라면
                if stone_count == 5:
                    #육목을 고려해야한다.
                    #육목을 탐색하기 전에 이전 값을 탐색해야 한다.
                    prev_x = x - dx[d]
                    prev_y = y - dy[d]
                    #1.이전 값의 범위가 오목판을 벗어나지 않으면 오목이다.
                    #2.이전 값의 오목판의 기준좌표와 다르면 오목이다.
                    if not(-1 < prev_x < n and -1 < prev_y < n) or board[x][y] != board[prev_x][prev_y]:
                        #기준좌표의 값을 계속 갱신해준다
                        answer = board[x][y]
                        #해당 오목이 검은돌인지 흰돌인지 출력
                        print(board[x][y])
                        #해당 위치의 좌표를 출력해준다. 현실 오목판은 19*19 x랑 y에 1을 더해준다
                        print(x + 1, y + 1)

#만약 answer에 아무 값도 담겨져 있지 않다면 무승부라는 것을 알 수 있다.
if answer == 0:
    print(answer) 