from itertools import combinations #조합을 쓰기 위해서 import
import sys
N, M = map(int, input().split())
result = [] #결과값을 받을 리스트
number = list(map(int, sys.stdin.readline().split())) #리스트로 값을 모아준다.

combination = list(combinations(number, 3)) #ㅊ3개의 숫자의 조합을 리스트에 담아준다

for i in combination: #리스트를 돌면서
    if sum(i) <= M: # 3개의 합이 m보다 작다면
        result.append(sum(i)) #추가해주고

print(max(result)) #최댓값을 출력해준다.



#다른 풀이
n, m = map(int, input().split())
num = list(map(int, input().split()))
l = len(num)
ans = 0
for i in range(0, l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if(num[i] + num[j] + num[k] > m):
                continue
            else:
                ans = max(ans, num[i] + num[j] + num[k])

print(ans)