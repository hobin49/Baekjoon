N = int(input())
# 물건을 옮기는데 최적의 방법은 가장 무거운 것을 들 수 있는 크레인이 가장 무거운 박스를 옮기는 것이다.
crane = sorted(list(map(int, input().split())), reverse=True)

M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

# 만약 박스 값이 크레인보다 크면 옮길 수 없는 박스이니 -1을 출력
if max(box) > max(crane):  # 담을 수 없는 경우
    print(-1)
    # else를 쓰지 않으면 시간 초과
else:
    answer = 0
    # 박스가 있을떄까지
    while len(box):
        answer += 1
        # 인덱스로 2중 for문을 돌면서 옮길수 있는 화물이 있는지 체크
        for i in range(len(crane)):
            for j in range(len(box)):
                # 만약 화물을 옮길 수 있으면
                if crane[i] >= box[j]:
                    # 해당 화물 삭제
                    # 예제 입력 1. [9, 8, 6], [7, 5, 4, 2, 2]
                    # [9:7, 8:5, 6:4] => answer += 1 => [9: 2, 8:2]
                    del box[j]
                    # break를 사용하지 않으면 list index out of range 발생
                    break
    print(answer)
