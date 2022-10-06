n = int(input())
lst = []
# 리스트에 입력값을 받아주고
for _ in range(n):
    level = int(input())
    lst.append(level)

# count 해줄 변수
cnt = 0
# 제일 높은 레벨부터 시작해서 바로 아래 레벨 점수와 비교한다.
for i in range(len(lst) - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        # 아래 레벨의 점수가 윗레벨의 점수보다 작아질때까지 감소
        while lst[i] <= lst[j]:
            lst[j] -= 1
            # count 해준다.
            cnt += 1
        else:
            continue

print(cnt)
