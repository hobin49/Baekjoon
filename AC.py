# D는 삭제 - popleft, R은 flip = list.reverse()
# 앞의 값을 삭제하기 위해 deque를 사용했다.
from collections import deque

#입력값을 받아주고 
T = int(input())
for _ in range(T):
    #함수를 입력값으로 받아주고 
    func = input()
    n = int(input())
    #입력에서 괄호와 쉼표를 모두 받는다 그래서 대괄호를 지우고 쉼표로 구분해준다. [1:-1]부분만 가져와서 deque를 만든다.
    numbers = input()[1:-1].split(",")
    #deque에 넣어준다.
    deq = deque(numbers)
    #reverse를 쓰면 시간초과가 뜨기 때문에 홀수 일때만 뒤집도록 수정하기 위해 변수를 만든다.
    cnt = 0

    # "[]"라고 입력을 받아도 deque의 길이는 1이 되기 때문에 길이가 0인 부분에 대해서는 예외사항으로 
    #빈큐로 초기화 해줘야 한다. 
    if n == 0:
        deq = deque()
    #함수는 문자열이다 그래서 문자열 한 개씩 돈다.    
    for a in func:
        #만약 함수가 reverse이면
        if a == "R":
            # 뒤집는 횟수를 1씩 증가해 누적시킨다.
            cnt += 1
        #만약 함수가 delete이면
        elif a == "D":
            # deq의 길이가 0이면 error를 출력하고 종료해준다
            if len(deq) == 0:
                print("error")
                break
            # 만약 deq가 있고 짝수인지 홀수인지 판별
            else:
                #짝수이면 어차피 리스트가 그대로이기 때문에 popleft를 활용해 좌측을 빼주고
                if cnt % 2 == 0:
                    deq.popleft()
                #홀수이면 뒤집기 때문에 뒤예 요소를 빼주는 것과 동일하다
                else:
                    deq.pop()


    #만약 break가 발생하지 않을 경우
    else:
        #만약 R의 개수가 짝수일 겨우 deq을 출력하고
        if cnt % 2 == 0:
            #deque(['1', '2', '3', '5', '8']) -> [1, 2, 3, 5, 8]이 되려면 리스트의 문자열을 합치는 
            #join함수를 사용한다 쉼표를 기준으로 그리고 출력값이 리스트 형태기 때문에 여는괄호 닫는괄호를 사용한다.
            print("[" + ",".join(deq) + "]")
        #홀수이면 한 번 뒤집고 출력한다. 
        else:
            deq.reverse()
            print("[" + ",".join(deq) + "]")


