N = 0
sum_ = 0
numbers = [] * 100001
for i in range(1, 10001):
    numbers.append(i)

for i in range(1, 10001):
    num = [(int(k)) for k in str(i)]
    sum_ = i + sum(num) # 57 = 51 + 6
    if sum_ in numbers:
        numbers.remove(sum_)
print(*numbers, sep = "\n")
        