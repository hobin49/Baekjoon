n = int(input())

number = list(map(int, input().split()))

sum_ = 0
cnt = 0
for i in range(n):
    if number[i] == 1:
        cnt += 1
        sum_ += cnt
    else:
        cnt = 0

print(sum_)
