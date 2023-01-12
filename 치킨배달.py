n, m = map(int, input().split())

distance = []
for _ in range(n):
    distance.append(list(map(int, input().split())))

# 거리 구한거 담을 리스트
result = []

# 집과 치킨집에 해당하는 좌표를 list에 담는다
houses = []
chickens = []
chicken_list = []
answer = 1e9
for i in range(n):
    for j in range(n):
        if distance[i][j] == 1:
            houses.append((i, j))

        elif distance[i][j] == 2:
            chickens.append((i, j))


# 거리 계산
def back(start, idx):
    global answer
    if start == m:
        sum_ = 0
        for house in houses:
            dis = 1e9
            for chicken in chickens:
                temp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
                # 도시의 치킨 거리 = dis의 합 = 각 잡당 치킨 거리의 최소 값의 합
                dis = min(temp, dis)
            sum_ += dis
        answer = min(answer, sum_)
        return

    # idx를 인자로 넣어주어 인덱스보다 더 적은 값은 들어오지 못하게 했고, 이미 같은 것을 가지고 있는 경우 continue를 통해 중복제거
    for i in range(idx, len(chickens)):
        if chickens[i] in chicken_list:
            continue

        chicken_list.append(chickens[i])
        back(start + 1, i + 1)
        chicken_list.pop()


back(0, 0)

print(answer)
