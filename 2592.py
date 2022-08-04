numbers = []
length = 10
for _ in range(length):
    k = int(input())
    numbers.append(k)
    lst_max = max(numbers, key=numbers.count)
    average = sum(numbers) // length
print(average, lst_max, sep="\n")
