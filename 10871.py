import sys
N, X = map(int, input().split())

for _ in range(N):
    A = list(map(int, sys.stdin.readline().split()))


    for i in A:
        if X > i:
           print(i, end = ' ')