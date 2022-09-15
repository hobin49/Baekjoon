import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst += list(map(int, input().split()))
    lst = sorted(lst, reverse=True)[:n]
print(lst[-1])

