import sys
input = sys.stdin.readline
for _ in range(int(input())):
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]
    step = 0

    
    for j in range(n):
        #층마다 비교하기 위해 floor
        floor = m - 1
         #행을 먼저 비교하다
        for i in range(m-1, -1, -1):
            # 만약에 박스가 있으면
            if box[i][j] == 1:
                #층에서 i를 빼면 거리가 나온다.
                step += floor - i
                print(step)
                #1층씩 빼준다.
                floor -= 1
    
    print(step)