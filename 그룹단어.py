# T = int(input())
# #값을 출력할 변수
# cnt = 0
# for _ in range(T):
#     word = input()
#     #그룹 단어가 아닌것을 체크하기 위한 변수
#     error = 0
#     #문자열을 인덱스로 접근해서 비교해준다
#     for idx in range(len(word)-1):
#         #만약 현재 요소와 다음 요소가 다르다면
#         if word[idx] != word[idx+1]:
#             #현재 글자 이후로 새로운 문자열 생성
#             new_word = word[idx+1]

#             #만약 새로운 문자열 중에 기존 문자열이랑 같은게 있다면 error += 1
#             if word.count(new_word[idx]) > 0:
#                 error += 1
#     if error == 0:
#         cnt += 1

# print(cnt)


N = int(input())
cnt = N

for _ in range(N):
    word = input()
    for i in range(len(word) -1):
        if word[i] == word[i+1]:
            pass
        #만약 i가 다음 요소에 있으면 문자열 개수에서 -=1 해주고 break
        elif word[i] in word[i+1:]:
            cnt -= 1
            break

print(cnt)

