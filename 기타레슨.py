import sys

input = sys.stdin.readline

# arr=[1, 2, 3, 4, 5, 6, 7, 8, 9], target = m
def binarysearch(arr, target):
    start = max(arr)
    end = sum(arr) // m + sum(arr) // n

    while start <= end:
        cnt = 1
        temp = 0
        mid = (start + end) // 2
        for a in arr:
            # 만약 합계가 중간값보다 작으면
            if temp + a <= mid:
                temp += a
            else:
                cnt += 1
                temp = a
        # 만약 카운트한게 블루레이 크기보다 작으면 끝에서 줄이고
        if cnt == target:
            return mid
        elif cnt > target:
            start = mid + 1
        # 아니면 늘리고
        else:
            end = mid - 1


n, m = map(int, input().split())

lecture = list(map(int, input().split()))

print(binarysearch(lecture, m))
