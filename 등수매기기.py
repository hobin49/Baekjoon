n = int(input())
lst = []
# 입력값을 받아준다.
for _ in range(n):
    num = int(input())
    lst.append(num)
# 각 사람이 예상한 등수를 오름차순으로 정렬한다.
lst.sort()

# 랭크를 사람의 수만큼 만든다.(1등부터 N등까지 동석차 없이 등수를 매겨야)
rank = [i for i in range(1, n + 1)]

# 불만도 계산하기 위한 변수
complain = 0

# 랭크에서 각 사람이 예상한 등수를 빼면 불만도에 최소를 구할수있다.
# 문제에서 불만도는 A와 B의 차이 (|A - B|)로 수치화
for i in range(n):
    # 1-0 = 1, 1-1 = 0, 2-1 = 1, 4-3 = 1 5-5= 0 => 누적값 3
    complain += abs(rank[i] - lst[i])

print(complain)
