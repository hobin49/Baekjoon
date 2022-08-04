#디버깅 시작
start = input()

# 문제의 개수 저장
problem = 0

# 디버깅이 끝날때까지 반복

while True:
    #문제, 고무오리 혹은 고무오리 디버깅 끝을 입력한다.
    duck = input()

    if duck == "고무오리 디버깅 끝":
        #반복문을 탈출
        break
    # 문제 혹은 고무오리를 입력했다면
    else:
        #문제를 입력했다면
        if duck == "문제":
            problem += 1
        #고무오리를 입력 했으면.
        elif duck == "고무오리":
            if problem == 0:#문제의 개수가 0개인 경우 체벌로 개수 2개를 더해준다.
                problem += 2
            else: 
                problem -= 1 #한 문제를 해결하므로 문제의 개수에서 1을 뺀다.


# 남은 문제의 개수가 0개라면
if problem == 0:
    #사랑해 출력
    print("고무오리야 사랑해")

# 남은 문제의 개수가 1개 이상이라면
else:
    # 힝구를 출력한다
    print("힝구")
        
            