import sys
input = sys.stdin.readline
n = []
for i in range(int(input())):
    n.append(list(map(int, input().split())))

# lambda 익명 함수를 활용한 정렬 x[0] 정렬후 x[1]도 정렬
n.sort(key= lambda x: (x[0], x[1]))
for a in n:
    print(a[0], a[1])
