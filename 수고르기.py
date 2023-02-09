import sys
input = sys.stdin.readline

n, m = map(int, input().split())

number = []
for _ in range(n):
    number.append(int(input()))

number.sort()

start, end = 0, 0
result = sys.maxsize

while start < n and end < n :
    temp = number[end] - number[start]
    if temp < m:
        end += 1

    else:
        result = min(result, temp)
        start += 1

print(result)


# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# number = []
# for _ in range(n):
#     number.append(int(input()))

# number.sort()

# start, end = 0, 1
# result = sys.maxsize

# while end < n:
#     temp = number[end] - number[start]
#     if temp < m:
#         end += 1
#         continue

#     if temp == m:
#         result = m
#         break

#     result = min(result, temp)
#     start += 1

# print(result)