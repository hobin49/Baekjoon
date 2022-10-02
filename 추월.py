# 입력값 받고
n = int(input())
# 입력한 차를 담을 딕셔너리
entrance = {}
# 테스만큼 돌면서
for i in range(n):
    # 입력값을 받고
    car_number = input()
    # {0: 'ZG431SN', 1: 'ZG5080K', 2: 'ST123D', 3: 'ZG206A'}
    entrance[i] = car_number

# 나온 차량을 담을 딕셔너리
exit_ = {}
for j in range(n):
    # 나머지 입력값을 또 받아주고
    car_number1 = input()
    # 딕셔너리에 담아준다.
    # {'ZG206A': 0, 'ZG431SN': 1, 'ZG5080K': 2, 'ST123D': 3}
    exit_[car_number1] = j


# 1 2 3 4
# 4 1 2 3 -> 4번차량은 + 1 (3개의 차를 추월), 2번 차량은 (count 0 ) 3번차량(0)

# 1 2 3 4
# 3 4 1 2 -> 4번 차량은 (+ 1) 3번차량은 (+ 1) 2번차량( 0) 1번차량(0)
# 추월한 차량을 담을 변수
cnt = 0
# 1번 차량은 첫 차량이니까 볼 필요가 없으니 그 다음 차량부터 본다. (1, 2, 3)
for p in range(1, n):
    for q in range(0, p):
        # 만약에 추월한 차량이 있다면
        if exit_[entrance[q]] > exit_[entrance[p]]:
            # count 해주고 종료해준다.
            print(exit_)
            cnt += 1
            break
print(cnt)
