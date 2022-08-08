T = int(input())
for _ in range(T):
    N, M = map(int , input().split())
    count = 0
    for i in range(N, M + 1):
        w = str(i)
        #count함수를 써서 사용 
        count += w.count('0')
    print(count)