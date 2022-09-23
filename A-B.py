from collections import deque
#입력값을 받아주고
a, B = map(int, input().split())
#연산횟수를 담을 변수를 만들어주고
res = -1
#바꿔야하는 값과 연산횟수를 담을 값을 넣는다.
queue = deque([(a, 1)])

#큐가 있을때까지 돌아준다.
while queue:
    #앞의 요소를 뺴준다.
    A, cnt = queue.popleft()

    #만약 A와 B의 값이 일치하면 
    if A == B:
        #누적된 연산 횟수를 갱신하고 종료
        res = cnt

    #만약 A에 2를 곱한 값이 B보다 작거나 같으면
    if (A * 2) <= B:
        #큐에 계산된 값과 연산횟수 + 1를 담아준다.
        queue.append((A * 2, cnt + 1))
    
    #만약 숫자와 숫자 가장 오른쪽 1을 더한 값이 b보다 작거나 같으면
    if int(str(A) + "1") <= B:
        #계산된 값과 연산횟수 +1을 담아준다.
        queue.append((int(str(A) + "1"), cnt + 1))
#만들 수 없는 경우에는 -1을 출력한다.
print(res)
