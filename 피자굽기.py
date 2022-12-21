# d, n = map(int, input().split())

# oven = list(map(int, input().split()))
# dough = list(map(int, input().split()))


# # 6짜리 피자가 어차피 위에 5가 있으면 들어갈 수 없으니까
# # [5, 5, 4, 3, 3, 2, 2]로 바꿔준다.
# for i in range(1, len(oven)):
#     if oven[i] > oven[i - 1]:
#         oven[i] = oven[i - 1]

# start, end = 0, len(oven) - 1
# # 도우가 쌓이는 곳
# piled_dough = 0
# for d in dough:
#     # False로 남으면 도우를 더 못쌓는다는 뜻
#     is_piled = False

#     while start <= end:
#         mid = (start + end) // 2
#         # 오븐의 중간 인덱스의 값이 dough 값보다 크다면
#         if oven[mid] >= d:
#             start = mid + 1
#             piled_dough = mid
#             is_piled = True
#         # 도우가 더 크면 들어갈 수 없으니까 줄여야한다.
#         else:
#             end = mid - 1

#     if not is_piled:
#         piled_dough = -1
#         break

#     start = 0
#     # 도우가 쌓이면 rp값 갱신
#     end = piled_dough - 1


# if piled_dough == -1:
#     print(0)
# else:
#     print(piled_dough + 1)


# //3%에서 틀림
d, n = map(int, input().split())

oven = list(map(int, input().split()))
dough = list(map(int, input().split()))

oven_depth = []
# 누적값으로 비교..
sum_ = 0
sum_list = []
# [5, 11, 15, 18, 24, 26, 29]
# 오븐 깊이의 누적값
for k in range(len(oven)):
    sum_ += oven[k]
    sum_list.append(sum_)

# 나중에 피자 반죽의 위치를 찾기 위해서 오븐의 깊이에 번호를 넣는다.
# [(1, 5), (2, 11), (3, 15), (4, 18), (5, 24), (6, 26), (7, 29)]
for idx, value in enumerate(sum_list, start=1):
    oven_depth.append((idx, value))


# 피자 반죽의 위치 누적값
sum1_ = 0
sum1_list = []
# [3, 5, 10]
for d in range(len(dough)):
    sum1_ += dough[d]
    sum1_list.append(sum1_)

# 최소값
last_dough = sum1_list[-1]


# 피자가 모두 오븐에 들어가지 않는 상황
if sum(oven) < sum(dough):
    print(0)
else:
    for o in range(len(oven_depth)):
        if last_dough <= oven_depth[o][1]:
            print(oven_depth[o][0])
            break
