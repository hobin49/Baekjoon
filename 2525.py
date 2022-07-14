#이 문제는 맞추지 못했다. 어떤 부분이 부족했는지 보자.
#정답 코드
H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)

# 내풀이 
# 일단 내 풀이는 쓸데없이 복잡하다. 조건문을 elif까지 써서 복잡하게 쓰지 않아도 된다.
# 변수 설정을 보면 나는 입력값을 B + C를 더한 값의 몫과 나머지를 구했고 위에는 하나의 값만 해줬다.
# 코드도 얼 비슷해 보이지만 위에 코드가 명확하고 답을 바로 구할 수 있다.
A, B = map(int, input().split())
C = int(input())

hour = (B + C) // 60
minute = (B + C) % 60
a_hour = A + hour
day = 24

if a_hour > 23 and (B + C) > 60:
    print(a_hour - day, minute)
elif (a_hour < 23 and (B + C) < 60):
    print(A, B + C)
elif (a_hour > 23 and (B + C) < 60):
    print(a_hour - day, B + C)