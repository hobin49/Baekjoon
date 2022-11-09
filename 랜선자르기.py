# 입력값을 받기
n, m = map(int, input().split())
# 초기값을 담을 리스트
lancable = []
# 랜선의 크기를 받고
for _ in range(n):
    lan = int(input())
    lancable.append(lan)

# 시작점
min_lan = 0
# 끝점
max_lan = max(lancable)

# while문을 돌면서
while min_lan <= max_lan:
    total = 0
    # 중간값
    mid = (min_lan + max_lan) // 2
    # 이미 가지고 있는 랜선의 개수만큼 돌면서
    for x in range(n):
        # 중간값으로 나눈 값들을 계속 더해주고
        total += lancable[x] // mid
    # 개수가 필요한 개수 이상이면 오른쪽 부분을 탐색하고
    if total >= m:
        min_lan = mid + 1
    # 개수가 필요한 개수 이하이면 왼쪽 부분을 탐색한다.
    else:
        max_lan = mid - 1
print(max_lan)
