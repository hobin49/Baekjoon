import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

numbers = []

num = 0
for i in range(n):
    for j in range(m):
        num += lst[i][j]
        numbers.append(num)

print(numbers)
