d, n = map(int, input().split())

oven = list(map(int, input().split()))

pizza = list(map(int, input().split()))

# 오븐 높이를 정렬하자

for i in range(d - 1):
    if oven[i + 1] > oven[i]:
        oven[i + 1] = oven[i]

# 오븐 정렬
# [2, 2, 3, 3, 4, 5, 5]
oven.sort()

# 이제 돌면서 피자가 오븐에 모두 들어가는지 체크
cnt = 0
# 오븐의 길이
oven_depth = len(oven)

# 피자를 다 돌면서
for i in range(len(oven)):
    # 만약에 나중에 체크한 값이 피자의 개수와 같으면 종료
    if cnt == len(pizza):
        # 출력
        print(oven_depth)
        break

    # 만약 oven 깊이가 피자의 도우보다 깊으면 1을 해준다.
    if pizza[cnt] <= oven[i]:
        cnt += 1
        # 깊이를 계속 갱신한다.
        # 피자는 아래에서부터 쌓인다 그리고 최종적으로 5가 쌓이는 구간은 2번째다.
        oven_depth = len(oven) - i

else:
    print(0)
