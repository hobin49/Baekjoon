S, E, Q = list(map(str, input().split()))
# 딕셔너리 2개를 받아주고
dict1 = {}
dict2 = {}
# 테스트케이스를 모르기 때문에 while문으로 동작
while True:
    try:
        time, member = list(map(str, input().split()))
        # 시작시간 전에 입장했으면 이름과 시간을 딕셔너리에 담아준다.
        if time <= S:
            dict1[member] = time
        # 만약에 끝나는 시간부터 스트리밍을 끝날때까지 있었던 사람들을 딕셔너리에 담아준다.
        elif time >= E and time <= Q:
            dict2[member] = time
    except:
        break

# 몇 명인지 세워줄 변수
cnt = 0
# 시작 시간 전에 입장한 사람들 중에서 퇴장까지 확인된 사람들을 확인해준다.
for key, value in dict1.items():
    if key in dict2.keys():
        cnt += 1

print(cnt)
