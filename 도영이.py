from itertools import combinations
n = int(input())

diff = []
m, k = 0, 0
#입력값을 받아주고
for _ in range(n):
    sour, bitter = map(int, input().split())
    diff.append([sour, bitter])


result = int(1e9)


for i in range(1, n+1):
    #콤비네이션을 사용해주고
    k = combinations(diff, i)
    for c in k:
        #신맛은 곱, 쓴맛은 합
        s, b = 1, 0
        #그래서 콤비네이션을 활용한 값을 돌면서
        for one, two in c:
            s *= one
            b += two
        #신맛과 - 쓴맛의 차이가 최소인 값을 구한다.
        result = min(result, abs(s-b))

print(result)