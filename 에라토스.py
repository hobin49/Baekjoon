n, k = map(int, input().split())

cnt = 0

nums = [True] * (n + 1)

for i in range(2, len(nums) + 1):
    for j in range(i, n + 1, i):
        if nums[j] == True:
            nums[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                brea
