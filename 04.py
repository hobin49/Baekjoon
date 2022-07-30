import sys

sys.stdin = open('04_input.txt', 'r')
T = int(input())
for tc in range(1, T+ 1):
    number = list(map(int, input().split())) #리스트에 입력값을 받고

    even = sum(number[1:16:2]) #인덱스로 접근해서 짝수 요소의 합
    odd = sum([i * 2 for i in number[0:16:2]]) #홀수 요소의 합을 list comprehension 활용해서 *2를 해준 것을 합했다.
    
    remain = (even + odd) % 10 # 홀수랑 짝수 더한 것을 10로 나눈 나머지를 구하기
    if remain != 0 : # 나머지가 0 이 아니면
        answer = 10 - remain # 10에서 빼주고
    else: # 나머지가 0이면 0 출력
        answer = 0
    print(f"#{tc} {answer}")
    
