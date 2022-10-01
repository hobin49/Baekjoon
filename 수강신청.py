K, L = map(int, input().split())
# 딕셔너리에 받아주고
dict_ = {}
for i in range(L):
    # 숫자형으로 받지 말고 문자형으로 받아야
    number = input()
    # 리스트를 넣어서 돌린게 패착1
    dict_[number] = i + 1
# 순서들을 정렬해주고
sorted_dict = sorted(dict_.items(), key=lambda x: x[1])
# 학번만 뽑아주고
result = [elem[0] for elem in sorted_dict]

# 성공한 인원들만 뽑아준다.
print(*result[:K], sep="\n")


# 2번째 방법 런타임 에러...

# K, L = map(int, input().split())

# lst = []
# for i in range(L):
#     number = int(input())
#     lst.append(number)
# queue = deque(lst)
# check = []
# while queue:
#     now = queue.popleft()
#     if now in queue:
#         continue
#     else:
#         check.append(now)

# print(*check[:K], sep="\n")
