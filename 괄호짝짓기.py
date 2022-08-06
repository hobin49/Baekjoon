moves = [1,5,3,5,1,2,1,4]

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
n  = 5
k = 0
result = []
answer = 0

for i in moves:
    for j in range(n):
        if board[j][i-1] != 0:
            result.append(str(board[j][i-1]))
            board[j][i-1] = 0
            break
    
while len(result) != k:
    if result[k] == result[k+1]:
        result.pop(k)
        result.pop(k)
        k = 0
        answer += 2

        if len(result) == 0:
            break
    else:
        k += 1

print(answer)