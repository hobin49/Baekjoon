import sys

input = sys.stdin.readline


n = int(input())

count = 0
while n > 1:
    count += n // 5
    n //= 5
print(n)
print(count)
