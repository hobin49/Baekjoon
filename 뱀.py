# from collections import deque

# n = int(input())

# # 사과의 위치 정보 저장
# apple = []
# for _ in range(int(input())):
#     apple.append(list(map(int, input().split())))

# # 방향 변환 정보 저장
# turns = []
# for _ in range(int(input())):
#     x, c = input().split()
#     turns.append([int(x), c])

# # 뱀의 위치를 deque으로 저장하고 이동하면서 추가, 삭제
# snake = deque()
# snake.append([1, 1])

# # 방향 전환을 위한 move
# move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# # 시작은 오른쪽으로
# m = 0
# time = 0

# while True:
#     # 시작하면 시간을 한칸 늘려줌
#     time += 1

#     # 한칸 앞의 위치인 new 좌표를 저장
#     new = [snake[-1][0] + move[m][0], snake[-1][1] + move[m][1]]

#     # new 좌표가 범위를 벗어난다면 종료
#     if not (0 < new[0] <= n and 0 < new[1] <= n):
#         break

#     # new 좌표가 자기 자신의 좌표라면 종료
#     if new in snake:
#         break

#     # 범위를 벗어나지 않고 자기 자신의 좌표가 아니면 길이를 늘려 추가
#     snake.append(new)

#     # new가 사과가 아니라면 꼬리를 한 칸 줄임
#     if new not in apple:
#         snake.popleft()
#     # new가 사과라면 사과를 제거하고 그대로 길이를 늘림
#     else:
#         apple.pop(apple.index(new))

#     # 방향 전환
#     for turn in turns:
#         # 현재 시간을 측정해 방향 전환에 있는지 확인
#         if time == turn[0]:
#             # 방향을 D로 전환한다면 +1
#             if turn[1] == "D":
#                 m += 1
#             # 방향을 L로 전환한다면 -1
#             elif turn[1] == "L":
#                 m -= 1

#             # 방향 정보는 0 ~ 3이기 때문에 범위에 맞게 초기화
#             if m == 4:
#                 m = 0
#             elif m < 0:
#                 m = 3

# print(time)
from collections import deque

n = int(input())

k = int(input())

# 사과의 위치 저장
apple = []
for _ in range(k):
    apple.append(list(map(int, input().split())))

L = int(input())
# 방향 변환 정보 전환
turns = []
for _ in range(L):
    x, c = input().split()
    turns.append([int(x), c])

# 뱀의 위치를 저장하고 이동하면서 추가 삭제
snake = deque()
# 시작점
snake.append([1, 1])

# 방향 전환을 위한 이동리스트 (우, 하 , 좌, 상)-시작은 오른쪽으로
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 방향 전환을 위한 변수
m = 0

# 시간 측정을 위한 변수
time = 0

# while문 시작(무한루프)
while True:
    time += 1
    # 한 칸 앞의 위치를 new 좌표를 저장 (1, 1) -> (1, 2)
    new = [snake[-1][0] + move[m][0], snake[-1][1] + move[m][1]]

    # 만약 new가 좌표에서 벗어난다면 종료
    if not (0 < new[0] <= n and 0 < new[1] <= n):
        break

    # 만약 좌표가 자기 자신이라면 종료
    if new in snake:
        break

    # 범위와 좌표를 통과하면 추가한다
    snake.append(new)

    # new가 사과가 아니면 꼬리를 줄인다
    if new not in apple:
        snake.popleft()
    else:
        apple.pop(apple.index(new))

    # 방향 전환을 한다.
    for turn in turns:
        if time == turn[0]:
            if turn[1] == "D":
                m += 1
            else:
                m -= 1
            # 방향정보는 0~3 범위에 맞게 초기화한다.
            if m == 4:
                m = 0
            elif m < 0:
                m = 3

print(time)
