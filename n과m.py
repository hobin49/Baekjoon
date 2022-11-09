# def n_and_m(depth):

#     if len(answer) == m:
#         print(" ".join(map(str, answer)))

#     for i in range(1, n + 1):
#         if i not in answer:
#             answer.append(i)
#             n_and_m(i + 1)
#             answer.pop()
#         # if not visited[i]:
#         #     visited[i] = True
#         #     answer.append(i)
#         #     n_and_m(depth + 1, n, m)
#         #     # visited[i] = False
#         #     answer.pop()


# n, m = map(int, input().split())
# # # 중복 방지
# # visited = [False] * (n + 1)
# answer = []

# n_and_m(1)


N, M = map(int, input().split())
s = []


def back(start):
    if len(s) == M:  # 길이가 M이면 출력
        print(" ".join(map(str, s)))

    for i in range(start, N + 1):
        if i not in s:  # i가 리스트에 없으면 추가
            s.append(i)  # 재귀 실행
            back(i + 1)
            s.pop()


back(1)
