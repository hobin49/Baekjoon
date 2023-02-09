n = int(input())
lst = list(map(int, input().split()))

#누적합 구할 리스트가 필요
sum_ = [0 for _ in range(n+1)]

#누적합[1]에는 리스트[0]을 넣고
sum_[1] = 1

# 누적합[2]부터는 만약 리스트[i-2]가 리스트[i-1]랑 같은지
for i in range(2, n+1):
    if lst[i-2] == lst[i-1]:
        # sum_[i] = sum_[i-1] + 1
        sum_[i] = 1

left = 0
right = 0
for j in range(n):
    if lst[j] == 1:
        left += sum_[j+1]
    else:
        right += sum_[j+1]


print(abs(left-right))

