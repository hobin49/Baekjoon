n, m = map(int, input().split())

wood = list(map(int, input().split()))


start = 1
end = max(wood)

while start <= end:
    result = 0
    cut = 0
    mid = (start + end) // 2

    for w in wood:
        if w >= mid:
            cut += w - mid
    # 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
    if cut >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
