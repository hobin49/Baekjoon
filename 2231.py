result = []

for num in range(1, 10001):
    result.append(num)
    result = num + sum(result)
    if num != result:
        result.append(num)