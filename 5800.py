N = int(input())
for tc in range(1, N + 1):
    k = list(map(int, input().split()))
    grade = k.pop(0)
    max_ = 0
    k.sort(reverse=True)
    for i in range(len(k) - 1):
        if max_ < k[i] - k[i+1]:
            max_ = k[i] - k[i+1] 
    print(f"Class {tc}")
    print(f"Max {k[0]}, Min {k[-1]}, Largest gap {max_}")

