import sys
input = sys.stdin.readline
t = int(input())
time = []
#입력 값을 받고
for _ in range(t):
    n, m = list(map(int, input().split()))
    #리스트에 넣어준다.
    time.append([n, m])
#lambda를 활용해서 앞과 뒤를 정렬한다.
time = sorted(time, key = lambda x: x[0])
time = sorted(time, key= lambda x:x[1])

#시간 비교해줄 변수
last_time = 0 
#정답을 출력할 변수
cnt = 0

#시간 비교 
for start, end in time:
    #뒤에 요소를 보고 뒤에 요소보다 큰 값이 앞에 있으면 1을 추가
    if start > last_time:
        cnt += 1
        last_time = end

print(cnt)