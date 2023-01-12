n = int(input())

a = list(map(int, input().split()))

# 앞쪽에서 증가하는 함수
inc_dp = [1 for i in range(n)]
# 뒤쪽에서 증가하는 함수
dec_dp = [1 for i in range(n)]

# 이전에 증가하는 부분 수열 문제처럼 전에 값보다 뒤에 값이 크면 +1을해서 값을 넣어논다.
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            # [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

# 뒤에서 부터 증가하면 아래처럼 나와야 한다.
# [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]

# 아이디어가 떠오르지 않아 일단 뒤집어서 하기로 했습니다.
# [1, 5, 2, 1, 4, 3, 4, 5, 2, 1] -> [1, 2, 5, 4, 3, 4, 1, 2, 5, 1]
a_ = a[::-1]

for i in range(n):
    for j in range(i):
        if a_[i] > a_[j]:
            # [1, 2, 3, 3, 3, 4, 1, 2, 5, 1]
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

# [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]
dec_dp = dec_dp[::-1]


result = []
max_ = 0
for i in range(n):
    max_num = max(max_, inc_dp[i] + dec_dp[i])
    # [2, 7, 4, 2, 7, 6, 7, 8, 4, 2]
    result.append(max_num)

# 왼쪽에서는 1,2,4,5 뒤에서부터는 5,2,1이 선택되는데 5가 중복되므로 1을 뺴준다.
print(max(result) - 1)
