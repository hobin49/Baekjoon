import sys

input = sys.stdin.readline

# arr=[1, 2, 3, 4, 5, 6, 7, 8, 9], target = m
def binarysearch(arr, target):
    start, end = 0, len(arr) - 1
    cnt, sum_ = 0, 0
    while start <= end:
        mid = (start + end) // 2

        for i in range(n):
            # 15
            mid = (start + end) // 2
            sum_ += arr[i]
            # 만약 합계가 중간값보다 작으면
            if sum_ <= mid:
                # count+= 1 sum_초기화
                cnt += 1
                sum_ = 0
        # 만약 카운트한게 블루레이 크기보다 작으면 끝에서 줄이고
        if cnt <= target:
            end = mid - 1
        # 아니면 늘리고
        else:
            start = mid + 1
    return start


n, m = map(int, input().split())

lecture = list(map(int, input().split()))

print(binarysearch(lecture, m))
