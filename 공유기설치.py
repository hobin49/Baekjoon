import sys
input = sys.stdin.readline

n, c = map(int, input().split())

routes = []
for _ in range(n):
    a = int(input())
    routes.append(a)

print(routes)

# 오름차순 정렬
routes.sort()

#최소거리
left = 1
#끝지점[리스트의 (최댓값 - 최솟값)은 주어진 좌표에서 이동할 수 있는 최대거리]
right = routes[n-1] - routes[0]


#시작지점이 끝지점의 값보다 작거나 같을 때까지
while left <= right:
    #공유기를 count 해줄 값
    cnt = 1
    #가장 첫 번째 집에 공유기를 설치해야 한다.(가장 인접한 두 공유기 사이의 거리가 최대가 되기 위해서)
    start = routes[0]
    #중간값을 구해준다.
    mid = (left + right) // 2
    #주어진 리스트의 길이만큼 돌면서
    for i in range(1, len(routes)):
        #인접한 두 공유기 사이의 거리를 최대로 해야하기 때문에
        #2번째 집부터 마지막까지 탐색하면서 집과 현재 집의 거리가 mid 이상이라면
        if routes[i] - start >= mid:
            # 기준이 되는 집을 현재 집으로 변경한 후 계속 탐색한다.
            start = routes[i]
            #해당 집에 공유기 설치
            cnt += 1

    # 공유기의 수를 줄여야한다면 간격을 늘린다.
    if cnt >= c:
        ans = mid
        left = mid + 1
    # 공유기 수가 많으면 간격을 줄인다.
    else:
        right = mid -1

print(ans)





