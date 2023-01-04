n, m = map(int, input().split())

k = [list(map(str, input())) for _ in range(n)]
board = []

for row in range(n - 7):
    for column in range(m - 7):
        white_start = 0
        black_start = 0
        for r in range(row, row + 8):
            for c in range(column, column + 8):
                # 짝수인 경우에 일정한 색을 가지고 홀수여도 그렇다.
                if (r + c) % 2 == 0:
                    if k[r][c] != "W":
                        white_start += 1
                    elif k[r][c] != "B":
                        black_start += 1
                else:
                    if k[r][c] != "B":
                        white_start += 1
                    elif k[r][c] != "W":
                        black_start += 1
        board.append(white_start)
        board.append(black_start)

print(board)
