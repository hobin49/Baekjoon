def checking(idx, score, cal):
    global good_score
    # 정해진 칼로리른 넘어설 경우 리턴
    if cal > L:
        return
    # 최고 점수를 넘는다면 갱신해준다.
    if score > good_score:
        good_score = score

    # 인덱스가 N에 도달하면 리턴
    if idx == N:
        return

    # 재료를 넣지 않는 경우
    checking(idx + 1, score, cal)
    # 재료를 넣는 경우
    checking(idx + 1, score + list_[idx][0], cal + list_[idx][1])


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    list_ = []
    good_score = 0
    score = 0
    for _ in range(N):
        list_.append(list(map(int, input().split())))
    checking(0, 0, 0)
    print("#{} {}".format(tc, good_score))
