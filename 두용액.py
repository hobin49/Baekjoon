import sys

input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))

# 시작값
start = 0

# 끝값
end = n - 1

# 최대 정수값
min_ = sys.maxsize

# 서로 다른 두 용액이므로 등호를 빼야한다.
while start < end:
    # 나중에 비교를 위해서 절댓값으로 치환한다.
    temp = abs(arr[start] + arr[end])

    # 0과 가까운 최솟값을 구해야하므로 계속 최솟값을 갱신해준다.
    if temp < min_:
        min_ = temp
        answer = [arr[start], arr[end]]

    # 만약 계산 값이 0이면 종료한다.
    if temp == 0:
        break

    # 만약 계산한 값이 음수면 늘려주고 양수면 줄여준다.
    if temp < 0:
        start += 1
    else:
        end -= 1

for i in answer:
    print(i, end=" ")
