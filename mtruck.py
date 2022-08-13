#우, 우하, 하 방향 설정이 담긴 배열 자기자신(0,0)은 생략 가능
dx = [0, 1, 1]
dy = [1, 1, 0]

#행과 열을 입력 받아준다.
r, c = map(int, input().split())
#빌딩을 담은 변수
building = "#"
#부숴야 할 차를 담은 변수 
breaking = "X"


# #행을 가지고 이차원 리스트를 만든다.
parking = [list(input()) for _ in range(r)]

#부수고 주차할 수 있는 공간을 담을 변수가 필요하다.
breaking_list = [0] * 5

#행과 열을 이용하여 이중 for문 사용
for x in range(r):
    for y in range(c):
        #기준 좌표를 옮길 때마다 초기화 해주고 부순 차의 개수를 담을 변수 설정
        breaking_count = 0
        # 기준 좌표가 빌딩을 만나면 다음으로 지나간다.
        if parking[x][y] == building:
            continue
        
        # 기준좌표가 차를 만나면 카운트해준다.
        if parking[x][y] == breaking:
            breaking_count += 1

        #삼분탐색을 진행한다
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]

            # 만약 탐색의 범위가 주어진 배열의 범위가 아니라면 종료
            if not(-1 < nx < r and -1 < ny < c):
                break

            # 만약 빌딩을 만나면 종료해준다.
            if parking[nx][ny] == building:
                break
            
            # 만약 차를 만나면 count해준다.
            if parking[nx][ny] == breaking:
                breaking_count += 1

        #만약에 break되지 않으면 부순차의 개수를 담은 변수를 인덱스로 삼아 공간을 담을 변수에 저장한다.
        else:
            breaking_list[breaking_count] += 1

# for문을 이용해서 리스트를 돌아주면서 최종 값들을 출력한다.
for cnt in breaking_list:
    print(cnt)
        
