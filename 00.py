from collections import Counter
import sys
sys.stdin = open('00_input.txt', 'r')

T = int(input()) #입력값
for tc in range(1, T+1):
    k = int(input()) # 입력값 

    A = list(map(int, input().split())) #list를 사용해서 값을 리스트에 넣어준다
    cnt = Counter(A).most_common()[0][0] #counter함수를 사용해서 각 요소가 몇 개인지 세주고 most_common 메서드를 사용해서 가장 많이 있는 요소를 cnt변수에 담아준다
    print(f"#{tc} {cnt}") #fstring 활용해서 출력