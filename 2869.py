A, B, C = map(int, input().split())

count = 0
result = 0
while result <= C:
    result += A
    count +=1
    if result >= C:
        break
    result -= B
print(count)