N = int(input())
# 첫 단어
first = list(input())
answer = 0


for _ in range(N-1):
    #첫 번째 값의 모든 값들을 복사
    compare = first[:]
    #나머지 단어
    words = input()
    cnt = 0

    #만약에 단어안에 있는 알파벳 중에서
    for word in words:
        #첫 번째 값과 일치하는 값이 존재한다면
        if word in compare:
            #값을 제거
            compare.remove(word)
        #일치하지 않으면 count해준다
        else:
            cnt += 1

    #count한 값이 0개이면 다 소거된 것이고 또는 1개이거나 비교하는 값이 1개면 문자를 빼거나 더하고 하나의 문자를 바꿀 수 있다는 것이 된다.
    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
#     r.append(len(str_))
#     lst.append(str_)eeee


# first = lst[0]
# lst.pop(0)
# letter = []
# first_len = len(first)

# for i in first:
#     letter.append(i)

# answer = []
# for i in range(len(lst)):
#     s = r[i]
#     cnt = 0
#     for j in range(s):
#         if lst[i][j] in letter:
#             cnt += 1
#     answer.append(cnt)

# result = 0
# for a in answer:
#     if a >= first_len:
#         result += 1
# print(result)
# # for j in range(1, len(lst)):
