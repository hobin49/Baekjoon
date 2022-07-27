A, B, C = map(int, input().split())

height = (C - B -1) // (A - B) + 1
print(height)

#다른 사람의 풀이 
a, b , v = map(int, input().split())
k = (v - b) / (a - b)
print(int(k) if k == int(k) else int(k) + 1) #삼항 연산자
#즉 int가 아니면 int에 1을 더해준다.