# for _ in range(k):
#     numbers.append(list(map(int, input().split())))


max_, x, y = 0, 0, 0
for i in range(9):
    numbers = list(map(int, input().split()))
    for j in range(9):
        if max_ < numbers[j]:
            max_, x, y = numbers[j], i, j

print(max_)
print(x + 1, y + 1)
