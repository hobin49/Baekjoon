import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

k = int(input())

sum_ = [0 for _ in range(n+1)]

new = 0
for i in range(1, n+1):
    new += lst[i-1]
    sum_[i] = new


for _ in range(k):
    i, j = map(int, input().split())
    print(sum_[j] - sum_[i-1])
