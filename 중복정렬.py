n = int(input())
numbers = list(map(int, input().split()))

number = sorted(list(set(numbers)))

print(*number)
