import sys
input = sys.stdin.readline

n = []
for i in range(int(input())):
    n.append(list(map(int, input().split())))

n.sort(key = lambda x: (x[1], x[0]))
for a in n:
    print(a)