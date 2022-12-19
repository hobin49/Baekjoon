import sys

input = sys.stdin.readline

n, m = map(int, input().split())


k = list(map(int, input().split()))

answer = [0]
mysum = 0

for i in range(n):
    mysum += k[i]
    answer.append(mysum)


for i in range(m):
    a, b = map(int, input().split())
    print(answer[b] - answer[a - 1])


#     print(p)
