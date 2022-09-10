# 입력값을 받아주고
n, m = map(int, input().split())

# 구름이 오는지 측정하기 위한 변수
answer = [[0] * m for _ in range(n)]

#입력값 받아준다.
cloud = [list(map(str, input())) for _ in range(n)]

#이중 for문을 돌면서
for i in range(n):
#구름이 있는지 없는지 체크하기 위한 변수
    flag = False 
    #이동할 거리 측정하는 변수
    distance = 1
    for j in range(m):
         #만약에 구름이 없고 .이면 -1을 리스트에 넣어준다.
        if not flag and cloud[i][j] == ".":
            answer[i][j] = -1 
      #만약에 구름을 발견했으면 해당 리스트에 0을 넣어주고 거리 측정할 변수를 초기화 해준다.
        elif cloud[i][j] == "c":
            flag = True
            answer[i][j] = 0
            distance = 1
        #구름도 있고 만약에 .이면 거리를 게속 1씩 늘려줘서 리스트에 담아준다.
        elif flag and cloud[i][j] == ".":
            answer[i][j] = distance
            distance += 1
        
#출력 작업
for c in answer:
    print(*c)

