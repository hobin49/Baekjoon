def bubblesort(arr):
    n = len(arr)
    global cnt, answer
    # 배열의 크키만큼 반복
    for i in range(n - 1, 0, -1):

        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(i):
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if arr[j] > arr[j + 1]:
                cnt += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 서로 위치를 반환
                if cnt == k:
                    answer = " ".join(str(x) for x in arr)


answer = -1
cnt = 0
n, k = map(int, input().split())
arr = list(map(int, input().split()))
bubblesort(arr)
print(answer)
