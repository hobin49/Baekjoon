import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    #m= 1이면 모든 배열 공간을 대상으로 휘두를 수 있다 그런데 파리채의 크기가 커지면 탐색할 수 있는 배열의 공간이 줄어든다. 
    for i in range(n-m-1):
        for j in range(n-m+1):
            fly = 0
            for x in range(m):
                for y in range(m):
                    fly += board[i+x][j+y]

                if fly > result:
                    result = fly

    print(result)