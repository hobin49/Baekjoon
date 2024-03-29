#dp테이블을 입력에서 주어진 계단의 개수가 300이하이므로 301까지 초깃값이 0인 리스트를 만들어준다
dp = [0] * 301

#계단의 개수 301개를 담기 위해 초깃값이 0으로 된 301개를 만든다.
step = [0] * 301

#입력값을 받아준다.
n = int(input())

#for문으로 n의 크기만큼 돌아준다
for i in range(1, n + 1):
    #미리 만들어 놓은 계단 리스트에 각 인덱스에 해당하는 값을 넣어준다
    step[i] = int(input())

#1은 1가지 경우만 존재한다
dp[1] = step[1]
#2는 2번째 계단이나 1번째랑 2번째 계단의 합 중에서 더 큰 값을 dp[2]에 넣어준다
dp[2] = max(step[1] + step[2], step[2])

#3은 (1번과+3번 계단 ) (2번과+3번 계단) 중에서 큰 값을 넣어준다.
dp[3] = max(step[1] + step[3], step[2] + step[3])

#나머지 4부터 301까지 돌아주면서
for _ in range(4, 301):
    #점화식을 만든다
    dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])

print(dp[i])




#질문: 시간복잡도가 상당하여 필요로 하는 조합 혹은 순열의 개수가 약간만 많아져도 알고리즘 테스트에서 활용하기는 쉽지 않다는 ...
#n이 10 이상 20이상
