import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())

daily = []
# 입력값을 (선호도, 도수) 이렇게 해서 리스트에 담는다.
for _ in range(K):
    like, degree = map(int, input().split())
    daily.append((like, degree))

# 도수를 기준으로 오름차순 정렬
beers = sorted(daily, key=lambda x: x[1])
# 선호도 담을 리스트
likes = []
# 조건 만족하는지 안 하는지 체크
flag = False
# 선호도 담을 변수
love = 0
# 최종값 담을 변수
cnt = 0
# 맥주 리스트를 돌면서
for beer in beers:
    # 선호도를 더해주고
    love += beer[0]
    # 힙푸쉬를 통해서 해당 선호도를 리스트에 넣어주고
    heapq.heappush(likes, beer[0])
    # 만약 N개도 다 마시고 선호도의 합이 M을 넘었으면
    if len(likes) == N:
        if love >= M:
            # 두 조건을 만족하는 도수를 담는다.
            # likes = [(2, 5), (4, 3), (3, 3)] =>swap을 통해 바뀐다.
            # 5가 cnt에 들어간다.
            cnt = beer[1]
            # flag True로 바꿔주고
            flag = True
            # 최적값 찾았으면 종료
            print(cnt)
            break
        # 선호도 합보다 작으면 우선순위 큐에서 선호도가 가장 작은 원소를 pop한다.
        # heappop은 가장 작은 원소를 삭제한다. heapq에 튜플이 삽입될 경우엔, 튜플의 첫 번째 요소가 정렬의 기준이 된다.
        else:
            love -= heapq.heappop(likes)

# 조건을 만족하지 않으면 -1을 출력
if not flag:
    print(-1)
