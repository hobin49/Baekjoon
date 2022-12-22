n = int(input())

cnt = 0
for _ in range(n):
    k = list(map(str, input()))
    stack = [0]
    # 반복문으로 문자열을 확인
    for i in k:
        # 스택의 마지막 요소와 현재 탐색하고 있는 요소와 같으면 팝해준다
        if stack[-1] == i:
            stack.pop()
        # 그렇지 않다면 스택에 추가한다.
        else:
            stack.append(i)

    # 스택의 길이가 1이면 아치형으로 모두 연결된 것으로 좋은 단어이다.
    # 처음에 스택에 0을 넣었기 때문에 길이가 1
    if len(stack) == 1:
        cnt += 1

print(cnt)
