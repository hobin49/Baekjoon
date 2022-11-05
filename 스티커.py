def solution(sticker):
    table = [0 for _ in range(len(sticker))]
    #맨앞에 뜯는 경우
    table[0] = sticker[0]
    table[1] = table[0]

    # table[i] = i 번째 index까지의 배열에서 얻을 수 있는 최댓값이라고 하면 
    # 1) 만약 i-1번 index의 스티커를 땠을 경우 i번째 index스티커를 뗄 수는 없다. 즉 table[i-1]값 그대로
    # 2) i -1번 스티커를 떼지 않았을 경우 = i-2번까지의 최댓값 + i번째 스티커의 값 
    for i in range(2, len(sticker) - 1):
        # [14, 14, 19, 25, 25, 34, 34, 0]
        table[i] = max(table[i - 1], table[i - 2] + sticker[i])


print(solution(sticker))
