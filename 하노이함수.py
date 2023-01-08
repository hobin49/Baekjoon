n = int(input())


# 하노이 탑을 이동 시킬 함수
def hanoi(n, start, sub, end):
    # n이 1인 마지막의 경우
    if n == 1:
        # 이동을 출력하고 종료
        print(start, end)
        return

    # 제일 큰 원판인 n번 원판을 제외한 n - 1개의 원판을 end를 거쳐 sub에 이동
    hanoi(n - 1, start, end, sub)
    # 제일 큰 n번 원판을 end로 이동하면서 출력
    print(start, end)
    # n - 1개의 원판을 다시 start를 거처 end로 이동
    hanoi(n - 1, sub, start, end)


# 하노이 탑의 이동 횟수는 2**n - 1
print(pow(2, n) - 1)
# n개의 원판을 1, 2, 3번의 기둥을 가지고 이동
hanoi(n, 1, 2, 3)
# for a, b, in ans:
#     sys.stdout.write(" ".join([str(a), str(b), "\n"]))


# # 하노이
# # 1번에서 3번기둥으로 옮기는데 2번 기둥을 보조로 사용한다.
# hanoi(5, 1, 3, 2)

# # 원반이 하나일 때 아무 문제 없이 이동하며 된다.
def hanoi(원반개수, 시작, 목표, 보조):
    if 원반개수 == 1:
        print(시작, 목표)
        return
    else:
        # 원반의 개수가 2개라면 위에 작은 원반이 보조로 이동해야한다 목표에 큰게 쌓여 있어야 하기 때문이다. (1번 원반이 2번으로 이동)
        hanoi(원반개수 - 1, 시작, 보조, 목표)
        # 그리고 1번에 남아있는 큰 원반이 목표 기둥으로 이동한다.
        print(시작, 목표)
        # 목표 원반을 옮기거나 다른 원반이 목표 원반 위에 못 놓게 되는 경우가 있나? 없다!
        # 원래 시작기둥을 보조기둥으로 바꾸고 보조기둥을 시작기둥으로 바꾸고
        hanoi(원반개수 - 1, 보조, 목표, 시작)
