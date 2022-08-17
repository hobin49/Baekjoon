# 주어진 입력에서 N은 40보다 작거나 같기 때문에 숫자는 1부터 시작하니까 41까지 dp를 만들어준다.
dp = [0] * 41
# dp3까지 값을 구해준다.
dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [1, 2]
# dp4 부터 41까지 값을 구해준다.
for i in range(4, 41):
    # dp[4] = dp[3] + dp[2] => [1, 1] + [1, 2] = [2, 3]
    # 그래서 list comprehension을 활용하고 zip을 활용해서 두 리스트의 요소들을 더해준다. 
    # zip은 튜플형태로 반환하기 떄문에 겉에 리스트로 감싸준다.
    dp[i] = [x + y for x, y in zip(dp[i-1], dp[i-2])]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])