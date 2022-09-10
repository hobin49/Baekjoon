import sys
from collections import Counter
#공백제거해서 입력값을 받고 리스트로 받아야 정렬 가능 
word = list(map(str, sys.stdin.readline().strip()))
#오름차순 정렬
word.sort()
#Counter 함수를 사용 예제 3 ABACABA => "AABCBAA"
a = Counter(word)
#홀수의 문자 담을 변수열
center = ""
#홀수의 개수를 확인할 변수
cnt = 0
#반복문을 돌면서 각 문자의 개수를 확인
for key, value in a.items():
    # 만약 개수가 홀수이면
    if value % 2 == 1:
        # 문자를 담고
        center += key
        # 중간값에 해당하는 인덱스를 찾고
        k = word.index(key)
        #삭제 word.remove해줘도 돼
        del(word[k])
        #홀수의 개수를 카운트 해준다.
        cnt += 1
    #만약 홀수의 개수가 1보다 클 경우 팰린드롬이 불가능
    if cnt > 1:
        break
# 홀수의 개수가 1보다 큰 경우 팰린드롬이 불가능하다.
if cnt > 1:
    print("I'm Sorry Hansoo")
# 홀수의 개수가 1개 이하일 경우
else:
    # 팰린드롬을 만들 변수
    res = ""
    #반복문을 통해 팰린드롬을 반으로 나누었을때 짝수부분을 더해준다.
    for i in range(0, len(word), 2):
        res += word[i]
    #왼쪽 + 가운데 + 오른쪽
    print(res + center + res[::-1])