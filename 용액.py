import sys
input = sys.stdin.readline

n = int(input())

liquid = list(map(int, input().split()))



#시작값
start = 0
#끝값
end = n-1
min_ = sys.maxsize

# 같은 값을 더할 수 없으니까 <= 아니고 <이다
while start < end:
    sum_ = liquid[start] + liquid[end]

    if abs(sum_) < min_:
        min_ = abs(sum_)
        answer = liquid[start], liquid[end]

    # sum == 0이면 정답이므로 종료
    if sum_ == 0:
        break

    if sum_ < 0:
        start += 1
    else:
        end -= 1

print(*answer)