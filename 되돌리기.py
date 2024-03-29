# def undo(target):
#     # 시간을 가지고 result를 탐색하여 원하는 시간에 있는 arr를 가져옴
#     for i in range(len(result) - 1, -1, -1):
#         # 만약 되돌린 시간이 210초이고 저장된 시간이 200초면 210초에는 200초의 arr가 있음
#         if target > result[i][0]:
#             # 바로 arr 가져오기
#             return result[i][1]
#     # 저장된 모든 시간을 다 돌아도 되돌린 시간에 저장된 문자열이 없다면 "" 공백
#     else:
#         return ""


# n = int(input())

# result = []
# arr = ""

# for i in range(n):
#     order, text, time = input().split()

#     # 명령어가 'type'이라면 arr에 문자를 더하고 result에 시간과 함께 저장
#     if order == "type":
#         arr += text
#         result.append((int(time), arr))

#     # 명령어가 'undo'라면 현재 시간과 되돌릴 시간을 뺀 뒤 그 시간에 저장된 arr를 가져옴
#     else:
#         text, time = int(text), int(time)
#         arr = undo(time - text)
#         result.append((time, arr))

# # 가장 마지막에 가져온 결과가 [시간, 문자열]이므로 1번 인덱스를 가져옴
# print(result[-1][1])


def undo(target):
    # 결국 리스트의 뒤부터 돌면서
    for i in range(len(result) - 1, -1, -1):
        # (시간-작업시간) > type의 시간보다 크다: 우리가 되돌려야 하는 값
        if target > result[i][1]:
            return result[i][0]
    # 없으면 공백처리
    else:
        return ""


n = int(input())

arr = ""

result = []

for _ in range(n):
    text, work, time = input().split()

    if text == "type":
        arr += work
        result.append((arr, int(time)))
    else:
        work, time = int(work), int(time)
        arr = undo(time - work)
        result.append((arr, int(time)))

print(result[-1][0])
