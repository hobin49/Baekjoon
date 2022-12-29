from collections import deque

n = int(input())

k = int(input())

# 보드판
board = [[0] * (n + 1) for _ in range(n + 1)]

# 보드판에 사과 추가
for _ in range(k):
    n1, n2 = map(int, input().split())
    board[n1][n2] = 1

l = int(input())

direction = []
for _ in range(l):
    direction.append(list(map(str, input().split())))

# 시간을 정수로 변환
for i in range(len(direction)):
    direction[i][0] = int(direction[i][0])


# 방향 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# bfs로 접근
def bfs(x, y):

    queue = deque()
    queue.append((1, 1))

    # 방문 시간 체크
    cnt = 0
    # 뱀이 처음 시작하는 곳 방문 처리(나중에 꼬리 밟는것을 고려해서 처리)
    # 만약 다음칸에 사과가 있으면

    if board[1][2] == 1:
        board[1][1] = 2
        cnt += 1
    # 꼬리를 없애야하니까 다시 0처리 해준다.
    else:
        board[1][1] = 0
        board[1][2] = 2
        cnt += 1
    # 큐애 있을때까지
    while queue:
        x, y = queue.popleft()

        # 사방탐색(이 부분을 모르겠네요...)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 만약 자기 꼬리를 밟으면 종료
            if board[nx][ny] == 2:
                break
            # 벽을 만나면 break
            if not (-1 < nx < n and -1 < ny < n):
                break

            # 위에 두 과정을 통과했으면... 어떻게 다음을 처리하지...?
