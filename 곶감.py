# n 은 5
n = int(input())
# a라는 2차원 리스트 
a = [list(map(int, input().split())) for i in range(n)]

# m 개의 정보 
m = int(input())
for i in range(m):
    # h 행번호, t 방향, k(개)
    h, t, k = map(int, input().split())

    # 방향이 왼쪽 방향일 경우 0
    if t == 0:
        for _ in range(k):
            # 제일 앞값(인덱스 0번째)을 pop하여 제일 뒤에 넣어줘야 하기 떄문에 
            # append를 통해 넣어줍니다. 
            a[h-1].append(a[h-1].pop(0))      #하나의 회전이 일어나는 부분이며 k번 하겠다는 의미입니다. 
    #방향이 오른쪽 방향일 경우 1
    else:
        for _ in range(k):
            # 제일 뒤에있는 값을 앞으로 넣어줘야 하기 때문에 insert를 통해 코드를 작성합니다. 
            # (0, a[h-1].pop())
            # 0번 인덱스 자리에 pop() 제일 뒤에 있는 값을 pop 해주세요라는 의미 
            a[h-1].insert(0, a[h-1].pop())

# 여기에 다 누적할 것
res = 0 
start = 0
end = n
# i는 행번호 입니다. 
for i in range(n):
    # j는 열번호 입니다.
    for j in range(start, end):
        res += a[i][j]
    # 모래시계 모양이 좁혀 들어가는 부분    
    if i < (n // 2):
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
    print(f"후{i}, {start}, {end}")
    
       
        