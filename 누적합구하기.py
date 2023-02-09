
arr = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]

m = 4
n = 4

sum_ = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i  in range(1, m + 1):
    for j in range(1, n + 1):
        sum_[i][j] = arr[i-1][j-1] + sum_[i][j-1] + sum_[i-1][j] - sum_[i-1][j-1]

for i in range(1, n+1):
    print(sum_[i])