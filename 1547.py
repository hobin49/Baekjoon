ball = [1, 2, 3]
for _ in range(int(input())):
    a, b = map(int, input().split())
    #a의 인덱스를 가져오고   
    a_ = ball.index(a)
    #b의 인덱스를 가져오고
    b_ = ball.index(b)
    #컵의 위치를 바꾸고
    ball[a_], ball[b_] = ball[b_], ball[a_]

#공이 들어있는 컵 번호 출력
print(ball[0])