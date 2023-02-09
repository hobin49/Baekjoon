n, m = map(int, input().split())

arr = []
sum_ = [[0 for _ in range(m+1)] for _ in range(n+1) ]
for _ in range(n):
    k = list(map(int, input().split()))
    arr.append(k)


for i in range(1, n+1):
    for j in range(1, m+1):
        sum_[i][j] = arr[i-1][j-1] + sum_[i-1][j] + sum_[i][j-1] - sum_[i-1][j-1]


k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())

    print(sum_[x][y] + sum_[i-1][j-1] - sum_[i-1][y] - sum_[x][j-1])