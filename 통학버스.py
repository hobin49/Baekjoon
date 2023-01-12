# 내가 접근한 방법
# 1. 거리(s)를 기준으로 거리를 나눈다.(절댓값을 활용)
# 2. 먼 거리에 있는 사람부터 데려온다.
# 3. 왕복이니 2를 곱해야 한다.


import sys

input = sys.stdin.readline

N, K, S = map(int, input().split())

left = []
right = []

for i in range(N):
    a, b = map(int, input().split())
    if a < S:
        left.append([S - a, b])
    else:
        right.append([abs(S - a), b])

# 먼 순서부터 가려면 정렬 필요
left, right = sorted(left), sorted(right)


def bus(L):
    a = 0  # 총 이동 거리
    while L:
        a += L[-1][0]  # 가장 먼 지점까지 다녀옴
        k = K  # 버스에 남은 자리 k자리
        while k and L:  # 해당 지점까지 다녀오면서 k명을 데리고 옴
            if L[-1][1] < k:  # 해당 지점에 있는 학생 수가 k명보다 많은 경우
                L[-1][1] -= k  # 데리고 오면서 그 지점의 학생수를 k명만큼 뻄
                k = 0  # 남은 자리는 0자리
            else:
                k -= L[-1][1]  # 더 적은 경우 해당 지점의 학생 수를 모두 데리고 온 후 그 지점을 리스트에서 pop
                L.pop()
                L[-1][1] -= k  # 데리고 오면서 그 지점의 학생수를 k명만큼 뻄
                k = 0  # 남은 자리는 0자리

    return a * 2  # 왕복이므로 *2


print(bus(left) + bus(right))
