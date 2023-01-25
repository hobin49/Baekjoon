N = int(input())
# 입력값
people = list(map(int, input().split()))
# 사람 수
order = [n for n in range(N, 0, -1)]

# 역으로 정렬(정방향으로 가면 다른 값이 나온다. 그래서 키가 큰 순서부터 고려해줬다.)
people = people[::-1]

# 입력값과 사람수를 zip함수를 사용해서 묶기
# [(0, 7), (0, 6), (2, 5), (1, 4), (1, 3), (1, 2), (6, 1)]
ziplist = list(zip(people, order))

# 결과를 담을 리스트
answer = []

# insert 함수를 사용해서 넣어준다.
for i, v in ziplist:
    answer.insert(i, v)

# answer을 출력
print(*answer, sep=" ")
