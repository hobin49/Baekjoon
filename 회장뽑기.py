import sys

input = sys.stdin.readline

INF = sys.maxsize

n = int(input())

#2차원리스트를 만들고, 모든 값을 무한으로 초기화
friends = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(n + 1):
    friends[i][i] = 0


#입력값이 마지막 줄에는 -1이 두 개 들어있으므로
while True:
    a, b = map(int, input().split())
    # 만약에 마지막 줄이면 종료
    if a == -1 and b == -1:
        break

    #a랑 b가 친구면 1 or b랑 a가 친구면 1
    friends[a][b] = 1
    friends[b][a] = 1


#단계마다 거쳐 가는 노드를 기준으로 실행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

print(friends)
max_number = []

for i in range(1, n + 1):
    max_number.append(max(friends[i][1:]))
min_ = min(max_number)

#리스트의 최솟값과, 리스트에 최솟값이랑 일치하는 사람이 몇 명 있는지 확인
print(min_, max_number.count(min_))

result = []


for i in range(n):
    #회장 될 수 있는 사람이 몇 명인지 체크 후에
    if min_ == max_number[i]:
        # 0번 인덱스부터 시작이니까 +1을 한다.
        result.append(i + 1)

print(*result)
