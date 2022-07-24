T = int(input())
result = 0 
lines = 0


line = list(map(int, input().split()))

line.sort() # 오름차순 정렬

for i in line:
    lines += i #담긴 요소를 더하고 
    result += lines #더한 값을 다시 결과에 더해준다

print(result)